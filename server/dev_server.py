from __future__ import annotations
from http.server import BaseHTTPRequestHandler, HTTPServer
from socketserver import ThreadingMixIn
from typing import Any

from ..core.renderer import render
from ..routing.page import Page
from ..routing.router import Router


class _WebUIServer(ThreadingMixIn, HTTPServer):
    daemon_threads = True


class WebUIRequestHandler(BaseHTTPRequestHandler):
    page: Any = None

    def do_GET(self) -> None:
        target = self.page
        if isinstance(target, Router):
            page = target.route(self.path)
            if page is None:
                self.send_error(404, "Route not found")
                return
            target = page.component
        if isinstance(target, Page):
            target = target.component

        body = self._render_target(target)
        self.send_response(200)
        self.send_header("Content-Type", "text/html; charset=utf-8")
        self.send_header("Content-Length", str(len(body.encode("utf-8"))))
        self.end_headers()
        self.wfile.write(body.encode("utf-8"))

    def _render_target(self, target: Any) -> str:
        if hasattr(target, "render"):
            return render(target)
        return str(target)

    def log_message(self, format: str, *args: Any) -> None:
        return


def run(page: Any, host: str = "127.0.0.1", port: int = 8000) -> None:
    server = _WebUIServer((host, port), WebUIRequestHandler)
    WebUIRequestHandler.page = page
    print(f"Running WebUI at http://{host}:{port}")
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        print("Stopping WebUI server...")
        server.shutdown()

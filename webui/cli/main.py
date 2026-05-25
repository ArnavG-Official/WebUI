from __future__ import annotations
import argparse
import importlib.util
from pathlib import Path

from ..webui import run


def main() -> None:
    parser = argparse.ArgumentParser(prog="webui", description="Run a WebUI Python application.")
    parser.add_argument("file", help="Python file that defines a WebUI page.")
    parser.add_argument("--host", default="127.0.0.1", help="Host to bind the dev server.")
    parser.add_argument("--port", type=int, default=8000, help="Port to bind the dev server.")
    args = parser.parse_args()

    path = Path(args.file).resolve()
    spec = importlib.util.spec_from_file_location(path.stem, str(path))
    if spec is None or spec.loader is None:
        raise SystemExit(f"Unable to import {path}")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)

    page = getattr(module, "page", None)
    if page is None:
        raise SystemExit("The module must expose a `page` variable.")
    run(page, host=args.host, port=args.port)

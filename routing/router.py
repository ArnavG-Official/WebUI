from __future__ import annotations
from typing import Any

from .page import Page


class Router:
    def __init__(self) -> None:
        self.routes: dict[str, Page] = {}

    def add(self, path: str, page: Page) -> Page:
        self.routes[path] = page
        return page

    def route(self, path: str) -> Page | None:
        normalized = path.split("?")[0]
        if not normalized:
            normalized = "/"
        return self.routes.get(normalized)

    def all_routes(self) -> list[Page]:
        return list(self.routes.values())

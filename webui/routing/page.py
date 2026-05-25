from __future__ import annotations
from typing import Any


class Page:
    def __init__(self, path: str, component: Any) -> None:
        self.path = path
        self.component = component

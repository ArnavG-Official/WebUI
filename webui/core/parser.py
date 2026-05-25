from __future__ import annotations
from typing import Any

from .element import Element


def parse(value: Any) -> Element:
    if isinstance(value, Element):
        return value
    raise TypeError("Only Element instances can be parsed by WebUI parser.")

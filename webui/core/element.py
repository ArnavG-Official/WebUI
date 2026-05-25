from __future__ import annotations
from typing import Any

from ..utils.helpers import flatten, normalize_attr_name


class Element:
    def __init__(self, tag: str, *children: Any, **attrs: Any):
        self.tag = tag
        self.attrs = self._normalize_attrs(attrs)
        self.children = flatten(children)

    def _normalize_attrs(self, attrs: dict[str, Any]) -> dict[str, Any]:
        normalized: dict[str, Any] = {}
        for key, value in attrs.items():
            normalized[normalize_attr_name(key)] = value
        return normalized

    def render(self) -> str:
        from .renderer import render
        return render(self)

    def __str__(self) -> str:
        return self.render()

    def __repr__(self) -> str:
        return f"<Element tag={self.tag!r} attrs={self.attrs!r} children={self.children!r}>"


class Comment:
    def __init__(self, text: Any = ""):
        self.text = str(text)

    def render(self) -> str:
        from .renderer import render
        return render(self)

    def __str__(self) -> str:
        return self.render()

    def __repr__(self) -> str:
        return f"<Comment text={self.text!r}>"

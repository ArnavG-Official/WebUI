from __future__ import annotations
from typing import Any

from ..utils.escape import escape_attribute, escape_html
from ..utils.helpers import is_text, stringify
from .element import Comment, Element

SELF_CLOSING_TAGS = {
    "area", "base", "br", "col", "embed", "hr", "img", "input", "link", "meta", "param", "source", "track", "wbr"
}


def format_attrs(attrs: dict[str, Any]) -> str:
    parts: list[str] = []
    for key, value in attrs.items():
        if value is None or value is False:
            continue
        if value is True:
            parts.append(key)
            continue
        text = stringify(value)
        parts.append(f'{key}="{escape_attribute(text)}"')
    return " " + " ".join(parts) if parts else ""


def render(element: Any) -> str:
    if element is None:
        return ""
    if is_text(element):
        return escape_html(element)
    if isinstance(element, Comment):
        return f"<!--{element.text}-->"
    if isinstance(element, Element):
        attrs = format_attrs(element.attrs)
        if not element.children and element.tag in SELF_CLOSING_TAGS:
            return f"<{element.tag}{attrs} />"
        children = "".join(render(child) for child in element.children)
        return f"<{element.tag}{attrs}>{children}</{element.tag}>"
    if isinstance(element, (list, tuple)):
        return "".join(render(child) for child in element)
    return escape_html(str(element))

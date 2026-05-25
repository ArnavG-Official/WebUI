from __future__ import annotations
import html


def escape_html(text: str) -> str:
    return html.escape(str(text), quote=False)


def escape_attribute(text: str) -> str:
    return html.escape(str(text), quote=True)

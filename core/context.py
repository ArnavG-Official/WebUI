from __future__ import annotations


class RenderContext:
    def __init__(self, indent: int = 0, namespace: str | None = None) -> None:
        self.indent = indent
        self.namespace = namespace

    def with_indent(self) -> "RenderContext":
        return RenderContext(indent=self.indent + 1, namespace=self.namespace)

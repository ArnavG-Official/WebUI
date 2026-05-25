from __future__ import annotations

__all__ = [
    "color",
    "background",
    "opacity",
    "font_size",
    "font_weight",
    "font_family",
    "text_align",
    "margin",
    "padding",
    "gap",
    "display",
    "flex",
    "grid",
    "style",
]


def _style(property_name: str, value: str | None) -> str:
    if value is None:
        return ""
    return f"{property_name}:{value};"


def _normalize_property(name: str) -> str:
    if name.startswith("_"):
        name = "-" + name[1:]
    return name.replace("__", "-").replace("_", "-")


def color(value: str | None) -> str:
    return _style("color", value)


def background(value: str | None) -> str:
    return _style("background", value)


def opacity(value: str | None) -> str:
    return _style("opacity", value)


def font_size(value: str | None) -> str:
    return _style("font-size", value)


def font_weight(value: str | None) -> str:
    return _style("font-weight", value)


def font_family(value: str | None) -> str:
    return _style("font-family", value)


def text_align(value: str | None) -> str:
    return _style("text-align", value)


def margin(value: str | None) -> str:
    return _style("margin", value)


def padding(value: str | None) -> str:
    return _style("padding", value)


def gap(value: str | None) -> str:
    return _style("gap", value)


def display(value: str | None) -> str:
    return _style("display", value)


def flex(value: str | None) -> str:
    return _style("display", "flex") + _style("flex", value)


def grid(value: str | None) -> str:
    return _style("display", "grid") + _style("grid-template-columns", value)


def style(**attrs: str | None) -> str:
    return "".join(
        _style(_normalize_property(key), value)
        for key, value in attrs.items()
        if value is not None
    )


def __getattr__(name: str):
    if name in globals():
        raise AttributeError(f"module {__name__} has no attribute {name!r}")

    def property_fn(value: str | None) -> str:
        return _style(_normalize_property(name), value)

    return property_fn


def __dir__() -> list[str]:
    return sorted([*globals().keys(), "style"])

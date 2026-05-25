from __future__ import annotations
import json

EVENTS = [
    "onabort",
    "onanimationcancel",
    "onanimationend",
    "onanimationiteration",
    "onanimationstart",
    "onauxclick",
    "onbeforecopy",
    "onbeforecut",
    "onbeforeinput",
    "onbeforepaste",
    "onbeforeprint",
    "onbeforeunload",
    "onblur",
    "oncancel",
    "oncanplay",
    "oncanplaythrough",
    "onchange",
    "onclick",
    "onclose",
    "oncontextmenu",
    "oncopy",
    "oncuechange",
    "oncut",
    "ondblclick",
    "ondurationchange",
    "onemptied",
    "onencrypted",
    "onended",
    "onerror",
    "onfocus",
    "onfocusin",
    "onfocusout",
    "onformdata",
    "oninput",
    "oninvalid",
    "onkeydown",
    "onkeypress",
    "onkeyup",
    "onload",
    "onloadeddata",
    "onloadedmetadata",
    "onloadstart",
    "onmessage",
    "onmessageerror",
    "onmousedown",
    "onmouseenter",
    "onmouseleave",
    "onmousemove",
    "onmouseout",
    "onmouseover",
    "onmouseup",
    "onmousewheel",
    "onpause",
    "onplay",
    "onplaying",
    "onpopstate",
    "onprogress",
    "onratechange",
    "onreset",
    "onresize",
    "onscroll",
    "onseeked",
    "onseeking",
    "onselect",
    "onselectionchange",
    "onselectstart",
    "onstalled",
    "onsubmit",
    "onsuspend",
    "ontimeupdate",
    "ontoggle",
    "ontouchcancel",
    "ontouchend",
    "ontouchmove",
    "ontouchstart",
    "ontransitioncancel",
    "ontransitionend",
    "ontransitionrun",
    "ontransitionstart",
    "onunload",
    "onvolumechange",
    "onwaiting",
    "onwheel",
    "ongotpointercapture",
    "onlostpointercapture",
    "onpointercancel",
    "onpointerdown",
    "onpointerenter",
    "onpointerleave",
    "onpointermove",
    "onpointerout",
    "onpointerover",
    "onpointerup",
    "onsearch",
]

__all__ = ["JavaScript", "alert", "console_log", "raw", "event", *EVENTS]


class JavaScript:
    def __init__(self, expression: str) -> None:
        self.expression = expression

    def __str__(self) -> str:
        return self.expression


def _quote(value: str | int | float | bool) -> str:
    if isinstance(value, bool):
        return "true" if value else "false"
    if isinstance(value, (int, float)):
        return str(value)
    return json.dumps(str(value))


def alert(message: str | int | float | bool) -> JavaScript:
    return JavaScript(f"alert({_quote(message)})")


def console_log(message: str | int | float | bool) -> JavaScript:
    return JavaScript(f"console.log({_quote(message)})")


def raw(expression: str) -> JavaScript:
    return JavaScript(expression)


def event(name: str, expression: str | JavaScript) -> JavaScript:
    return JavaScript(str(expression))


def _make_event_handler(name: str):
    def event_fn(expression: str | JavaScript) -> JavaScript:
        return JavaScript(str(expression))

    event_fn.__name__ = name
    return event_fn


for _event_name in EVENTS:
    globals()[_event_name] = _make_event_handler(_event_name)


def __getattr__(name: str):
    if name in EVENTS:
        return globals()[name]
    raise AttributeError(f"module {__name__} has no attribute {name!r}")


def __dir__() -> list[str]:
    return sorted([*globals().keys(), *EVENTS])

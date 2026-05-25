from ..core.element import Element

__all__ = ["p", "span", "b", "i", "u", "code", "pre"]


def p(*children, **attrs):
    return Element("p", *children, **attrs)


def span(*children, **attrs):
    return Element("span", *children, **attrs)


def b(*children, **attrs):
    return Element("b", *children, **attrs)


def i(*children, **attrs):
    return Element("i", *children, **attrs)


def u(*children, **attrs):
    return Element("u", *children, **attrs)


def code(*children, **attrs):
    return Element("code", *children, **attrs)


def pre(*children, **attrs):
    return Element("pre", *children, **attrs)

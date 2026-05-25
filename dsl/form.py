from ..core.element import Element

__all__ = ["form", "input", "textarea", "button", "select", "option", "label"]


def form(*children, **attrs):
    return Element("form", *children, **attrs)


def input(*children, **attrs):
    return Element("input", *children, **attrs)


def textarea(*children, **attrs):
    return Element("textarea", *children, **attrs)


def button(*children, **attrs):
    return Element("button", *children, **attrs)


def select(*children, **attrs):
    return Element("select", *children, **attrs)


def option(*children, **attrs):
    return Element("option", *children, **attrs)


def label(*children, **attrs):
    return Element("label", *children, **attrs)

from ..core.element import Element

__all__ = [
    "div",
    "section",
    "article",
    "header",
    "footer",
    "main",
    "nav",
    "h1",
    "h2",
    "h3",
    "h4",
    "h5",
    "h6",
    "a",
    "ul",
    "ol",
    "li",
]


def div(*children, **attrs):
    return Element("div", *children, **attrs)


def section(*children, **attrs):
    return Element("section", *children, **attrs)


def article(*children, **attrs):
    return Element("article", *children, **attrs)


def header(*children, **attrs):
    return Element("header", *children, **attrs)


def footer(*children, **attrs):
    return Element("footer", *children, **attrs)


def main(*children, **attrs):
    return Element("main", *children, **attrs)


def nav(*children, **attrs):
    return Element("nav", *children, **attrs)


def h1(*children, **attrs):
    return Element("h1", *children, **attrs)


def h2(*children, **attrs):
    return Element("h2", *children, **attrs)


def h3(*children, **attrs):
    return Element("h3", *children, **attrs)


def h4(*children, **attrs):
    return Element("h4", *children, **attrs)


def h5(*children, **attrs):
    return Element("h5", *children, **attrs)


def h6(*children, **attrs):
    return Element("h6", *children, **attrs)


def a(*children, **attrs):
    return Element("a", *children, **attrs)


def ul(*children, **attrs):
    return Element("ul", *children, **attrs)


def ol(*children, **attrs):
    return Element("ol", *children, **attrs)


def li(*children, **attrs):
    return Element("li", *children, **attrs)

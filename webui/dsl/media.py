from ..core.element import Element

__all__ = ["img", "video", "audio", "source"]


def img(*children, **attrs):
    return Element("img", *children, **attrs)


def video(*children, **attrs):
    return Element("video", *children, **attrs)


def audio(*children, **attrs):
    return Element("audio", *children, **attrs)


def source(*children, **attrs):
    return Element("source", *children, **attrs)

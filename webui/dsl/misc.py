from __future__ import annotations

from typing import Any

from ..core.element import Comment, Element

__all__ = [
    "comment",
    "abbr",
    "address",
    "area",
    "aside",
    "base",
    "bdi",
    "bdo",
    "blockquote",
    "body",
    "br",
    "canvas",
    "caption",
    "cite",
    "col",
    "colgroup",
    "data",
    "datalist",
    "dd",
    "delete",
    "del_",
    "details",
    "dfn",
    "dialog",
    "dl",
    "dt",
    "em",
    "embed",
    "fieldset",
    "figcaption",
    "figure",
    "head",
    "hgroup",
    "hr",
    "iframe",
    "ins",
    "kbd",
    "legend",
    "link",
    "map",
    "mark",
    "menu",
    "meta",
    "meter",
    "noscript",
    "object",
    "optgroup",
    "output",
    "param",
    "picture",
    "progress",
    "q",
    "rp",
    "rt",
    "ruby",
    "s",
    "samp",
    "search",
    "small",
    "strong",
    "sub",
    "summary",
    "sup",
    "svg",
    "table",
    "tbody",
    "td",
    "template",
    "tfoot",
    "th",
    "thead",
    "time",
    "title",
    "tr",
    "track",
    "var",
    "wbr",
    "html",
    "script",
    "style",
]

def comment(text: Any = "") -> Comment:
    return Comment(text)


def _tag(name: str):
    def fn(*children: Any, **attrs: Any):
        return Element(name, *children, **attrs)

    fn.__name__ = name
    return fn

abbr = _tag("abbr")
address = _tag("address")
area = _tag("area")
aside = _tag("aside")
base = _tag("base")
bdi = _tag("bdi")
bdo = _tag("bdo")
blockquote = _tag("blockquote")
body = _tag("body")
br = _tag("br")
canvas = _tag("canvas")
caption = _tag("caption")
cite = _tag("cite")
col = _tag("col")
colgroup = _tag("colgroup")
data = _tag("data")
datalist = _tag("datalist")
dd = _tag("dd")
delete = _tag("del")
del_ = delete
details = _tag("details")
dfn = _tag("dfn")
dialog = _tag("dialog")
dl = _tag("dl")
dt = _tag("dt")
em = _tag("em")
embed = _tag("embed")
fieldset = _tag("fieldset")
figcaption = _tag("figcaption")
figure = _tag("figure")
head = _tag("head")
hgroup = _tag("hgroup")
hr = _tag("hr")
iframe = _tag("iframe")
ins = _tag("ins")
kbd = _tag("kbd")
legend = _tag("legend")
link = _tag("link")
map = _tag("map")
mark = _tag("mark")
menu = _tag("menu")
meta = _tag("meta")
meter = _tag("meter")
noscript = _tag("noscript")
object = _tag("object")
optgroup = _tag("optgroup")
output = _tag("output")
param = _tag("param")
picture = _tag("picture")
progress = _tag("progress")
q = _tag("q")
rp = _tag("rp")
rt = _tag("rt")
ruby = _tag("ruby")
s = _tag("s")
samp = _tag("samp")
search = _tag("search")
small = _tag("small")
strong = _tag("strong")
sub = _tag("sub")
summary = _tag("summary")
sup = _tag("sup")
svg = _tag("svg")
table = _tag("table")
tbody = _tag("tbody")
td = _tag("td")
template = _tag("template")
tfoot = _tag("tfoot")
th = _tag("th")
thead = _tag("thead")
time = _tag("time")
title = _tag("title")
tr = _tag("tr")
track = _tag("track")
var = _tag("var")
wbr = _tag("wbr")
html = _tag("html")
script = _tag("script")
style = _tag("style")

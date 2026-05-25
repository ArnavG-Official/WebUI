from ..html import div, h3, p


def card(title: str, body: str | None = None, footer: str | None = None, **attrs):
    children = [h3(title)]
    if body is not None:
        children.append(p(body))
    if footer is not None:
        children.append(div(footer, class_="webui-card-footer"))
    classes = attrs.pop("class", attrs.pop("class_", "webui-card"))
    if classes:
        classes = f"webui-card {classes}" if classes != "webui-card" else "webui-card"
    return div(*children, class_=classes, **attrs)

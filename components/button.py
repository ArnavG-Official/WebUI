from ..html import button as html_button


def button(label: str, **attrs):
    classes = attrs.pop("class", attrs.pop("class_", ""))
    if classes:
        classes = f"webui-button {classes}"
    else:
        classes = "webui-button"
    return html_button(label, class_=classes, **attrs)

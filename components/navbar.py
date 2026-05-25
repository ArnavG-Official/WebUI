from ..html import nav, ul, li, a


def navbar(*items, **attrs):
    links = []
    for item in items:
        if isinstance(item, tuple) and len(item) == 2:
            text, href = item
            links.append(li(a(text, href=href)))
        else:
            links.append(item)
    return nav(ul(*links), **attrs)

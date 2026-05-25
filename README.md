# WebUI
> A Python Library for creating webpages.

Build websites using pure Python. WebUI is a Python library that lets developers create HTML, CSS, and JavaScript using clean Python syntax.

Instead of writing:

```html
<h1>Hello</h1>
```

you write:

```python
webui.html.h1("Hello")
```

---

# Features

- HTML using Python
- CSS using Python
- JavaScript using Python
- Automatic HTML rendering
- Component-based architecture
- Clean syntax
- Localhost web server
- Reactive UI system (planned)
- Hot reload (planned)

---

# Installation

```bash
pip install webui
```

---

# Quick Example

```python
import webui

page = webui.html.div(

    webui.html.h1(
        "Hello WebUI"
    ),

    webui.html.p(
        "Build websites with Python!"
    ),

    webui.html.button(
        "Click Me",

        onclick=webui.js.alert(
            "Hello!"
        )
    )

)

webui.run(page)
```

---

# Syntax Structure

WebUI is separated into 3 modules:

| Module | Purpose |
|---|---|
| `webui.html` | HTML elements |
| `webui.css` | CSS styling |
| `webui.js` | JavaScript |

---

# HTML API

## Text

```python
webui.html.p()
webui.html.span()
webui.html.b()
webui.html.i()
webui.html.u()
webui.html.code()
webui.html.pre()
```

---

## Headings

```python
webui.html.h1()
webui.html.h2()
webui.html.h3()
webui.html.h4()
webui.html.h5()
webui.html.h6()
```

---

## Layout

```python
webui.html.div()
webui.html.section()
webui.html.article()
webui.html.header()
webui.html.footer()
webui.html.main()
webui.html.nav()
```

---

## Forms

```python
webui.html.form()
webui.html.input()
webui.html.textarea()
webui.html.button()
webui.html.select()
webui.html.option()
```

---

## Lists

```python
webui.html.ul()
webui.html.ol()
webui.html.li()
```

---

## Tables

```python
webui.html.table()
webui.html.tr()
webui.html.td()
webui.html.th()
```

---

# CSS API

## Colors

```python
webui.css.color()
webui.css.background()
webui.css.opacity()
```

---

## Typography

```python
webui.css.font_size()
webui.css.font_weight()
webui.css.font_family()
webui.css.text_align()
```

---

## Spacing

```python
webui.css.margin()
webui.css.padding()
webui.css.gap()
```

---

## Layout

```python
webui.css.flex()
webui.css.grid()
webui.css.display()
```

---

## Borders

```python
webui.css.border()
webui.css.border_radius()
webui.css.shadow()
```

---

## Animation

```python
webui.css.transition()
webui.css.transform()
webui.css.animate()
```

---

# JavaScript API

## Events

```python
webui.js.onclick()
webui.js.onhover()
webui.js.onchange()
webui.js.onsubmit()
```

---

## Browser Actions

```python
webui.js.alert()
webui.js.prompt()
webui.js.confirm()
webui.js.redirect()
```

---

## DOM Functions

```python
webui.js.hide()
webui.js.show()
webui.js.toggle()
webui.js.set_html()
```

---

# Styling Example

```python
import webui

page = webui.html.div(

    webui.html.h1(
        "Styled Title",

        style=[
            webui.css.color("blue"),
            webui.css.font_size("40px"),
            webui.css.margin("20px")
        ]
    )

)

webui.run(page)
```

---

# Button Example

```python
import webui

page = webui.html.button(

    "Click Me",

    style=[
        webui.css.background("black"),
        webui.css.color("white"),
        webui.css.padding("12px"),
        webui.css.border_radius("10px")
    ],

    onclick=webui.js.alert(
        "Hello!"
    )

)

webui.run(page)
```

---

# Output HTML

WebUI automatically generates:

- HTML
- CSS
- JavaScript

and launches a localhost server.

---

# Planned Features

- Components
- State management
- Virtual DOM
- Routing
- Tailwind support
- Hot reload
- WebSocket support
- Async rendering
- Theme engine

---

# Example Project Structure

```text
myproject/
│
├── app.py
├── index.html
└── assets/
```

---

# Example Architecture

```text
webui/
│
├── html/
├── css/
├── js/
├── renderer.py
├── server.py
└── state.py
```

---

# WebUI
> A Python Library for creating webpages.

Build websites using pure Python. WebUI is a Python library that lets developers create HTML, CSS, and JavaScript using clean Python syntax.

---

## Features

- HTML with Tag helper support using Python
- CSS with Property helper support using Python
- JavaScript using Python
- Full DOM event helper support
- Automatic HTML rendering
- Component-based architecture
- Clean syntax
- Localhost web server
- Reactive UI system
- Hot reload

---

## Installation

```bash
pip install webui=1.0
```

---

## Quick Example

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

## Syntax Structure

WebUI is separated into 3 modules:

| Module | Purpose |
|---|---|
| `webui.html` | HTML elements |
| `webui.css` | CSS styling |
| `webui.js` | JavaScript |

---

## HTML API

WebUI now supports all HTML5 tags via `webui.html.<tag>()`.
The examples below show common tag categories.

### Text

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

### Headings

```python
webui.html.h1()
webui.html.h2()
webui.html.h3()
webui.html.h4()
webui.html.h5()
webui.html.h6()
```

---

### Layout

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

### Forms

```python
webui.html.form()
webui.html.input()
webui.html.textarea()
webui.html.button()
webui.html.select()
webui.html.option()
```

---

### Lists

```python
webui.html.ul()
webui.html.ol()
webui.html.li()
```

---

### Tables

```python
webui.html.table()
webui.html.tr()
webui.html.td()
webui.html.th()
```

---

## CSS API

WebUI supports all CSS properties through helper functions like `webui.css.<property_name>()` and the generic `webui.css.style(...)` helper.

### Colors

```python
webui.css.color("red")
webui.css.background("#f0f0f0")
webui.css.opacity("0.8")
```

---

### Typography

```python
webui.css.font_size("16px")
webui.css.font_weight("bold")
webui.css.font_family("Arial, sans-serif")
webui.css.text_align("center")
```

---

### Spacing

```python
webui.css.margin("16px")
webui.css.padding("12px")
webui.css.gap("8px")
```

---

### Layout

```python
webui.css.display("grid")
webui.css.flex("1")
webui.css.grid("1fr 1fr")
```

---

### Dynamic Properties

```python
webui.css.background_color("red")
webui.css._webkit_transform("rotate(45deg)")
webui.css.style(border_top="1px solid black", padding="4px")
```

---

## JavaScript API

WebUI supports all DOM event helpers via `webui.js.on<event>()`.

### Events

```python
webui.js.onclick("alert('clicked')")
webui.js.oninput("console.log('input changed')")
webui.js.onsearch("console.log('search')")
webui.js.onsubmit("alert('submitted')")
```

---

### Utilities

```python
webui.js.alert("Hello")
webui.js.console_log("Message")
webui.js.raw("console.log('raw JS')")
webui.js.event("onclick", "alert('hi')")
```

---

## Styling Example

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

## Button Example

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

## Program Output

Any Python program created from this library will have a HTML output. The first time you excecute your Python file will run the server and luanch the HTML page. If you want to stop your running server just execute your Python file again.

---

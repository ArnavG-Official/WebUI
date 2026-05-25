webui/
│
├── __init__.py
├── core/
│   ├── __init__.py
│   ├── parser.py          # converts DSL → internal AST
│   ├── renderer.py        # AST → HTML output
│   ├── element.py         # base UI element class
│   └── context.py         # shared render context
│
├── dsl/
│   ├── __init__.py
│   ├── text.py            # webui.txt.bold(), italic(), etc.
│   ├── layout.py          # div, section, grid helpers
│   ├── form.py            # input, button, form DSL
│   └── media.py           # image, video, etc.
│
├── components/
│   ├── __init__.py
│   ├── button.py
│   ├── navbar.py
│   ├── card.py
│   └── input.py
│
├── state/
│   ├── __init__.py
│   ├── state.py           # simple reactive store
│   └── hooks.py           # use_state-like helpers (optional later)
│
├── routing/
│   ├── __init__.py
│   ├── router.py          # page routing system
│   └── page.py            # page definition system
│
├── server/
│   ├── __init__.py
│   ├── dev_server.py      # live preview server (Flask/FastAPI)
│   └── hot_reload.py      # optional auto refresh
│
├── utils/
│   ├── __init__.py
│   ├── escape.py          # HTML escaping
│   └── helpers.py
│
└── cli/
    ├── __init__.py
    └── main.py            # "webui run app.py"

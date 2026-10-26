# Ara_imgui

**Ara_imgui** is a lightweight and easy-to-use wrapper around [Dear ImGui](https://github.com/ocornut/imgui) using Python and GLFW. It simplifies GUI application development with ImGui by providing a convenient interface for managing windows, fonts, and application lifecycle.

## Features

- Simple ImGui app launch with a single `run` function
- Support various themes
- System or custom font loading, including Cyrillic support
- Value widgets return the new value directly; use `imgui.is_item_changed()` to react to edits
- Context managers for child regions, tables and tree nodes
- Ready-to-run examples included in the `examples` folder

## Installation

```bash
pip install ara_imgui
```

> ⚠️ Make sure you have Python 3.7+ and OpenGL support (e.g., via GPU drivers on Windows).

## Documentation

For detailed documentation, please refer to the [Ara_imgui documentation](https://hanamileh.github.io/Ara_imgui/).
This documentation includes information on how to use the library, available features and widgets.

## Usage

### Basic example

```python
from ara_imgui import App, imgui

app = App("Hello world example")

def gui():
    imgui.text("Hello, world!")
    if imgui.button("Click me"):
        print("Clicked!")

app.run(gui)
```

### Stateful widgets

Value widgets such as `input_text`, `combo`, `slider_float` and `color_edit3`
return the new value directly. To know whether the user changed it, call
`imgui.is_item_changed()` right after the widget:

```python
from ara_imgui import App, imgui

app = App("Widget example")

name = "Michail"
option = 0

def gui():
    global name, option

    name = imgui.input_text("Name", name)
    if imgui.is_item_changed():
        print(f"Name changed to {name}")

    option = imgui.combo("Option", option, ["One", "Two", "Three"])

app.run(gui)
```

Widgets that do not report a changed flag (buttons, tree nodes, layout helpers)
keep their usual ImGui return value.

### Flag enums

Flag enums live in `ara_imgui.flags` and are grouped by the widget or feature
they belong to:

```python
from ara_imgui import flags

input_flags = (
    flags.input_text.chars_no_blank
    | flags.input_text.password
)
password = imgui.input_text("Enter your password", password, flags=input_flags)
```

Available groups: `backend`, `button`, `child`, `color_edit`, `combo`,
`config`, `dock_node`, `drag_drop`, `draw`, `draw_list`, `focused`, `font`,
`font_atlas`, `hovered`, `input`, `input_text`, `item`, `list_clipper`,
`multi_select`, `popup`, `selectable`, `slider`, `tab_bar`, `tab_item`,
`table`, `table_column`, `table_row`, `tree_node`, `viewport`, `window`.

Each group is the same enum class as `imgui_bundle`'s `*Flags_`, so the raw
spellings (`imgui.InputTextFlags_`) keep working too.

### IDE support

`ara_imgui.imgui` ships type hints (`imgui.pyi` and a `py.typed` marker), so
VS Code / Pylance shows the same parameter names and return types as
`imgui_bundle`, adjusted for the value-only returns, `is_item_changed()` and
the context managers. `imgui.raw` is typed as the untouched
`imgui_bundle.imgui` module.

### Context managers

`imgui.child()`, `imgui.table()` and `imgui.tree()` can be used as context
managers, so the matching `end_child()` / `columns(1)` / `tree_pop()` call is
made for you:

```python
with imgui.child("Log", size=imgui.ImVec2(0, 120)):
    imgui.text("Child content")
```

`imgui.table()` wraps the legacy `imgui.columns()` API. Columns are set up for
you, and when `headers` is given they are rendered as the first row. Cells are
submitted with `imgui.next_column()`, which automatically wraps to a new line
after the last column:

```python
with imgui.table("People", 3, ["Name", "Age", "Sex"]):
    for name, age, sex in people:
        imgui.text(name)
        imgui.next_column()

        imgui.text(str(age))
        imgui.next_column()
        
        imgui.text(sex)
        imgui.next_column()
```

`columns` may be omitted when `headers` is given
(`imgui.table("People", headers=[...])`). Borders are enabled by default; pass
`borders=False` to disable them. If you need the modern table API instead
(sorting, resizing, scrolling), use `imgui.begin_table()` / `imgui.end_table()`
directly.

A collapsed tree node must not draw its content, so guard the body. The context
manager is truthy only while the node is open:

```python
with imgui.tree("Settings") as node:
    if node:
        imgui.text("Advanced options")
```

`imgui.child()` is truthy while visible as well, so the same guard can be used
around expensive content.

### Custom fonts and themes

```python
from ara_imgui import App, imgui, themes

font_path = R"C:\Windows\Fonts\Arial.ttf"

app = App("Font Example")
app.apply_theme(themes.cherry)
app.load_font(font_path, font_size=20)

def gui():
    imgui.text("Sample text with custom font")

app.run(gui)
```

### Themes

`themes` is an enum (`themes = Theme`), so `themes.dark`, `themes.light`,
`themes.cherry` and so on can be passed to `app.apply_theme()`. The plain name
string still works as well: `app.apply_theme("dark")`.

Available themes:

`dark`, `light`, `classic`, `material_flat`, `photoshop_style`,
`gray_variations`, `gray_variations_darker`, `microsoft_style`, `cherry`,
`darcula`, `darcula_darker`, `light_rounded`, `so_dark_accent_blue`,
`so_dark_accent_yellow`, `so_dark_accent_red`, `black_is_black`,
`white_is_white`.

Some of them map to differently named internal `imgui_bundle` themes (for
example `themes.dark` uses `hello_imgui.ImGuiTheme_.imgui_colors_dark`); the
mapping is handled for you.

## Examples

See the [`examples/`](./examples) folder:

* `hello_world.py` — Basic "Hello, world!" with a button.
* `basic_window.py` — Simple window with input field.
* `custom_font.py` — Font and multilingual text rendering.
* `widget_examples.py` — Most of the common widgets.
* `table_example.py` — Table with headers built with `imgui.table()`.
* `flags_example.py` — A compact tour of the `ara_imgui.flags` groups.

## Dependencies

* `imgui`
* `glfw`
* `imgui_bundle`

## License

MIT License. Free to use and modify.
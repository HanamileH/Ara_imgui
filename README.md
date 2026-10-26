# Ara_imgui

**Ara_imgui** is a lightweight and easy-to-use wrapper around [Imgui bundle](https://github.com/pthom/imgui_bundle).
It provides a more convenient and compact API for creating applications with Dear ImGui, and fixes some
interface shortcomings that make working with imgui bundle difficult.
The main goal of this library is simplified and more consistent work with the existing framework, without discarding its capabilities and power.

## Features
- Simple launch of an ImGui application with a single `run` function
- Ability to easily change the appearance, including themes and font
- Value widgets return the new value directly; to react to changes, use `imgui.is_item_changed()` (see below for details)
- Context managers for child regions, tables, and tree nodes
- Fixes for various other small things
- Ready-to-run examples in the `examples` folder

## Installation

```bash
pip install ara_imgui
```

> ⚠️ Make sure you have Python 3.7+ and OpenGL support.

## Documentation

See the [Ara_imgui documentation](https://hanamileh.github.io/Ara_imgui/) for detailed documentation.
The documentation includes information about using the library, available features, and widgets.

## Usage

### Quick start

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

Value widgets such as `input_text`, `combo`, `slider_float`, and `color_edit3`
return the new value directly. To find out whether the user changed it, call
`imgui.is_item_changed()` immediately after the widget:

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

Widgets that do not report a changed flag (buttons, tree nodes, layout helper elements)
keep the usual ImGui return value.

If you need the old familiar behavior, you can import `imgui` from `imgui_bundle`:
```python
from ara_imgui import App
from imgui_bundle import imgui

app = App("Widget example")

name = "Michail"
option = 0

def gui():
    global name, option

    changed, name = imgui.input_text("Name", name)

    if changed:
        print(f"Name changed to {name}")

    _, option = imgui.combo("Option", option, ["One", "Two", "Three"])

app.run(gui)
```

### Flag enums

Flag enums are located in `ara_imgui.flags` and are grouped by the widget or function
to which they relate:

```python
from ara_imgui import imgui, flags

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

Each group is the same enum class as `*Flags_` in `imgui_bundle`, so the original
spellings (`imgui.InputTextFlags_`) also continue to work.
You can still import flags from `imgui` if you wish.

### Context managers

`imgui.child()`, `imgui.table()`, and `imgui.tree()` can be used as context
managers, so the corresponding `end_child()` / `columns(1)` / `tree_pop()`
call is done for you:

```python
with imgui.child("Log", size=imgui.ImVec2(0, 120)):
    imgui.text("Child content")
```

`imgui.table()` wraps the `imgui.columns()` API. Columns are set up
for you, and if `headers` is specified, they are drawn as the first row. Cells
are passed using `imgui.next_column()`, which automatically wraps to a new row
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

`columns` can be omitted if `headers` is specified
(`imgui.table("People", headers=[...])`). Borders are enabled by default; pass
`borders=False` to disable them. If you need the modern table API
(sorting, resizing, scrolling), use `imgui.begin_table()` / `imgui.end_table()`
directly.

A collapsed tree node should not draw its contents, so guard the body. The context
manager is truthy only while the node is open:

```python
with imgui.tree("Settings") as node:
    if node:
        imgui.text("Advanced options")
```

`imgui.child()` is also truthy while visible, so the same guard can be used
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

`themes` is an enum, so `themes.dark`, `themes.light`,
`themes.cherry`, etc. can be passed to `app.apply_theme()`. A plain
string name also works: `app.apply_theme("dark")`.

Available themes (list from `imgui_bundle`):
- `dark`
- `light`
- `classic`
- `material_flat`
- `photoshop_style`
- `gray_variations`
- `gray_variations_darker`
- `microsoft_style`
- `cherry`
- `darcula`
- `darcula_darker`
- `light_rounded`
- `so_dark_accent_blue`
- `so_dark_accent_yellow`
- `so_dark_accent_red`
- `black_is_black`
- `white_is_white`

Some of them map to differently named internal `imgui_bundle` themes (for example,
`themes.dark` uses `hello_imgui.ImGuiTheme_.imgui_colors_dark`). This is intentional
to preserve backward compatibility with older versions of `Ara_imgui`.

## Examples

See the [`examples/`](./examples) folder:

* `hello_world.py` — Basic "Hello, world!" with a button.
* `basic_window.py` — A simple window with an input field.
* `custom_font.py` — Font rendering and multilingual text.
* `widget_examples.py` — Most common widgets.
* `table_example.py` — A table with headers built using `imgui.table()`.
* `flags_example.py` — A compact overview of the `ara_imgui.flags` groups.

## Dependencies

* `imgui_bundle`
* `imgui`
* `glfw`

## License

MIT License. Free to use and modify.
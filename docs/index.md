# Ara_imgui

**Ara_imgui** is a lightweight and easy-to-use wrapper around
[Dear ImGui](https://github.com/ocornut/imgui) and
[ImGui Bundle](https://github.com/pthom/imgui_bundle). It provides a compact
Python API for building desktop tools: windows, buttons, text fields, sliders,
tables, trees, popups, and more.

You do not need prior Dear ImGui experience. The documentation explains each
widget, its parameters, and complete runnable examples.

## Features

- Start an application with a single `App.run()` call
- Value widgets return their new value directly
- Value widgets can remember their previous value when it is omitted
- Explicit IDs, plus a convenient `++` counter for repeated widgets
- Context managers for child windows, tables, and tree nodes
- Named flag groups for input, sliders, tables, and other widgets
- Themes and custom fonts

## Installation

```bash
pip install ara_imgui
```

> ⚠️ Python 3.7+ and OpenGL support are required.

## Quick start

```python
from ara_imgui import App, imgui

app = App("Hello world")

def gui():
    imgui.text("Hello, world!")
    if imgui.button("Click me"):
        print("Clicked!")

app.run(gui)
```

`App.run()` opens a window and calls `gui()` once per frame. Every call draws
the interface for that frame; see [Core concepts](concepts.md) for the mental
model.

## Learn the basics

- [Core concepts](concepts.md) — frame loop, labels and IDs, values, vectors,
  flags, and context managers
- [Widget overview](widgets/index.md) — every widget grouped by category
- [Cheat sheet](cheat_sheet.md) — a one-page lookup table

## Value widgets

Widgets such as `input_text`, `input_int`, `slider_float`, `combo`, and
`checkbox` return their new value directly:

```python
from ara_imgui import App, imgui

app = App("Value widgets")

def gui():
    name = imgui.input_text("Name", default="")
    age = imgui.input_int("Age##input_id", default=18)

    imgui.text(f"Hello, {name or 'unknown'}! Age: {age}")

app.run(gui)
```

The value argument is optional. Omit it, or pass `None`, and the widget reuses
the value from the previous frame. Use `default=` for the first frame:

```python
name = imgui.input_text("Name")                    # remembered automatically
age = imgui.input_int("Age##input_id", default=18) # 18 on the first frame
```

You can change the remembered value from code:

```python
imgui.set_item_value("Age##input_id", 18)
```

To detect edits, call `imgui.is_item_changed()` immediately after the widget.
See [Value memory](widgets/value_memory.md),
[imgui.set_item_value](widgets/set_item_value.md), and
[imgui.is_item_changed](widgets/is_item_changed.md).

## Labels and IDs

Every interactive widget needs an ID that is unique inside its window. The
visible label doubles as the ID by default. Use `##` to keep a stable ID while
changing the visible text:

```python
imgui.input_text("Name##player_name")
```

For widgets created in a loop, a label ending in `++` generates an ID
automatically:

```python
for row in rows:
    imgui.input_text("Name++", row["name"])
    if imgui.button("Delete++"):
        ...
```

This is convenient while the order of rows is stable. When rows can be
inserted, removed, or reordered, use an explicit ID instead:

```python
for row in rows:
    imgui.input_text(f"Name##row_{row.id}", row["name"])
    if imgui.button(f"Delete##row_{row.id}"):
        ...
```

See [Labels and IDs](widgets/labels_and_ids.md) for the escape sequence,
warnings, and the full rules.

## Flags

Some widgets accept an optional `flags` bit mask. Named flag groups live in
`ara_imgui.flags`:

```python
from ara_imgui import App, flags, imgui

app = App("Flags")

def gui():
    input_flags = flags.input_text.chars_no_blank | flags.input_text.password
    password = imgui.input_text("Password", flags=input_flags)
    imgui.text(f"Length: {len(password)}")

app.run(gui)
```

Available groups: `backend`, `button`, `child`, `color_edit`, `combo`,
`config`, `dock_node`, `drag_drop`, `draw`, `draw_list`, `focused`, `font`,
`font_atlas`, `hovered`, `input`, `input_text`, `item`, `list_clipper`,
`multi_select`, `popup`, `selectable`, `slider`, `tab_bar`, `tab_item`,
`table`, `table_column`, `table_row`, `tree_node`, `viewport`, `window`.

The original `imgui.InputTextFlags_` names also work.

## Context managers

`imgui.child()`, `imgui.table()`, and `imgui.tree()` clean up their matching
`end` call for you:

```python
with imgui.child("Log", size=imgui.ImVec2(0, 120)):
    imgui.text("Child content")

with imgui.table("People", 3, ["Name", "Age", "Sex"]):
    imgui.text("John")
    imgui.next_column()
    imgui.text("25")
    imgui.next_column()
    imgui.text("Male")
    imgui.next_column()

with imgui.tree("Settings") as opened:
    if opened:
        imgui.text("Advanced options")
```

See [Child window](widgets/child.md), [Tables](widgets/table.md), and
[Trees](widgets/tree.md) for details.

## Fonts and themes

```python
from ara_imgui import App, imgui, themes

app = App("Font example")
app.apply_theme(themes.cherry)
app.load_font(R"C:\Windows\Fonts\Arial.ttf", font_size=20)

def gui():
    imgui.text("Custom font and theme")

app.run(gui)
```

`themes` is an enum. A plain string name also works:
`app.apply_theme("dark")`.

Available themes:

- `dark`, `light`, `classic`
- `material_flat`
- `photoshop_style`
- `gray_variations`, `gray_variations_darker`
- `microsoft_style`
- `cherry`
- `darcula`, `darcula_darker`
- `light_rounded`
- `so_dark_accent_blue`, `so_dark_accent_yellow`, `so_dark_accent_red`
- `black_is_black`, `white_is_white`

The names match ImGui Bundle's theme names. `themes.dark`, for example, uses
`hello_imgui.ImGuiTheme_.imgui_colors_dark` internally.

## Examples

The repository contains ready-to-run examples:

- [hello_world.py](https://github.com/HanamileH/Ara_imgui/blob/main/examples/hello_world.py) — basic "Hello, world!" with a button
- [basic_window.py](https://github.com/HanamileH/Ara_imgui/blob/main/examples/basic_window.py) — a simple window with an input field
- [custom_font.py](https://github.com/HanamileH/Ara_imgui/blob/main/examples/custom_font.py) — custom fonts and multilingual text
- [widget_examples.py](https://github.com/HanamileH/Ara_imgui/blob/main/examples/widget_examples.py) — most common widgets
- [table_example.py](https://github.com/HanamileH/Ara_imgui/blob/main/examples/table_example.py) — a table with headers
- [flags_example.py](https://github.com/HanamileH/Ara_imgui/blob/main/examples/flags_example.py) — an overview of the flag groups

## Dependencies

- Python 3.7+
- OpenGL support
- ImGui Bundle (installed automatically with `pip install ara_imgui`)

## License

MIT License. Free to use and modify.

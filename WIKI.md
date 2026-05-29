# Ara_imgui Wiki

This page explains how to use `ara_imgui` to build ImGui-based desktop UIs in Python.

The examples below are based on the scripts in `examples/` and show the most common widgets, layout helpers, and library-level features.

## 1. Overview

`Ara_imgui` is a small wrapper around Dear ImGui + GLFW. It gives you:

- a simple `App` entry point
- support for multiple ImGui windows through `Window`
- theme switching
- font loading, including Cyrillic support
- access to the underlying `imgui` module for all standard widgets

### Basic flow

1. Create an `App`
2. Optionally configure theme and fonts
3. Write a callback that draws your UI with `imgui`
4. Call `app.run(gui)`

```python
from ara_imgui import App, imgui

app = App("Hello world example")

def gui():
    imgui.text("Hello, world!")

app.run(gui)
```

## 2. Core Library API

### `App`

The main application object. It owns the main window, initializes the ImGui integration, and runs the event loop.

#### Inputs

- `title` (`str`): window title
- `width` (`int`): initial window width
- `height` (`int`): initial window height
- `log_level` (`str`): logging level

#### Outputs

- Creates and manages the main application window
- Exposes methods such as `run`, `apply_theme`, `load_font`, and `add_window`

#### Example

```python
from ara_imgui import App

app = App("My App", 800, 600)
```

### `Window`

A helper class for creating extra ImGui windows with their own UI callback.

#### Inputs

- `title` (`str`): window title
- `flags` (`int`): ImGui window flags
- `frame_ui` (`callable`): function used to draw window content

#### Outputs

- A reusable window object that can be added to the app with `app.add_window(window)`

#### Example

```python
from ara_imgui import Window, imgui

def extra_ui():
    imgui.text("Hello from a separate window")

extra_window = Window("Extra Window", frame_ui=extra_ui)
extra_window.set_pos(50, 50)
extra_window.set_size(300, 200)
```

### `App.run(render, update, terminate)`

Starts the main loop.

#### Inputs

- `render` (`callable`): draws the main window UI
- `update` (`callable`, optional): called during the update stage
- `terminate` (`callable`, optional): called on shutdown

#### Outputs

- Runs the application until the user closes the window

#### Example

```python
from ara_imgui import App, imgui

app = App("Run Example")

def gui():
    imgui.text("Main UI")

app.run(gui)
```

### Theme and font helpers

#### `app.apply_theme(name)`

Applies an ImGui theme.

- `name`: `"dark"` or `"light"`

#### `app.load_font(font_path=None, font_size=14, cyrillic_ranges=True)`

Loads a font into the ImGui font atlas.

- `font_path`: path to a `.ttf` font file, or `None` to use a platform default
- `font_size`: font size in pixels
- `cyrillic_ranges`: enables Cyrillic glyph ranges when `True`

#### Example

```python
from ara_imgui import App, imgui

app = App("Styled App")
app.apply_theme("light")
app.load_font(font_size=20)

def gui():
    imgui.text("Custom theme and font")

app.run(gui)
```

## 3. Widget Usage Rules

Most ImGui widgets follow the same pattern:

- pass a label as the first argument
- provide current state as input when needed
- unpack the return value to detect changes

Common return pattern:

```python
changed, value = imgui.some_widget(...)
```

For action widgets like `button`, the return value is typically a boolean:

```python
if imgui.button("Save"):
    print("Saved")
```

## 4. Common Widgets

### `imgui.text`

Displays static text.

#### Inputs

- `label` (`str`): text to render

#### Outputs

- None

#### Example

```python
imgui.text("This is a text label")
```

### `imgui.separator`

Draws a horizontal separator line.

#### Inputs

- None

#### Outputs

- None

#### Example

```python
imgui.text("Top section")
imgui.separator()
imgui.text("Bottom section")
```

### `imgui.same_line`

Places the next widget on the same horizontal line.

#### Inputs

- Optional spacing/position arguments, depending on the binding version

#### Outputs

- None

#### Example

```python
if imgui.button("Left"):
    print("Left clicked")

imgui.same_line()

if imgui.button("Right"):
    print("Right clicked")
```

### `imgui.button`

Creates a clickable button.

#### Inputs

- `label` (`str`): button caption

#### Outputs

- `bool`: `True` on the frame when the button is clicked

#### Example

```python
if imgui.button("Click me"):
    print("Button clicked")
```

### `imgui.checkbox`

Creates a checkbox with a boolean state.

#### Inputs

- `label` (`str`)
- `value` (`bool`): current checked state

#### Outputs

- `changed` (`bool`): whether the value changed
- `value` (`bool`): updated checked state

#### Example

```python
checked, show_grid = imgui.checkbox("Show grid", show_grid)
```

### `imgui.radio_button`

Creates a radio button for choosing one option from a group.

#### Inputs

- `label` (`str`)
- `active` (`bool`): whether this option is currently selected

#### Outputs

- `bool`: `True` when the radio button is activated

#### Example

```python
if imgui.radio_button("Low quality", selected_mode == 0):
    selected_mode = 0

if imgui.radio_button("Medium quality", selected_mode == 1):
    selected_mode = 1

if imgui.radio_button("High quality", selected_mode == 2):
    selected_mode = 2
```

### `imgui.input_text`

Text field for string input.

#### Inputs

- `label` (`str`)
- `value` (`str`): current text

#### Outputs

- `changed` (`bool`)
- `value` (`str`): updated text

#### Example

```python
changed, username = imgui.input_text("Enter your name", username)
```

### `imgui.input_int`

Numeric input for integers.

#### Inputs

- `label` (`str`)
- `value` (`int`)

#### Outputs

- `changed` (`bool`)
- `value` (`int`)

#### Example

```python
changed, counter = imgui.input_int("Counter", counter)
```

### `imgui.input_float`

Numeric input for floating-point values.

#### Inputs

- `label` (`str`)
- `value` (`float`)

#### Outputs

- `changed` (`bool`)
- `value` (`float`)

#### Example

```python
changed, speed = imgui.input_float("Speed", speed)
```

### `imgui.slider_int`

Integer slider.

#### Inputs

- `label` (`str`)
- `value` (`int`)
- `min_value` (`int`)
- `max_value` (`int`)

#### Outputs

- `changed` (`bool`)
- `value` (`int`)

#### Example

```python
changed, volume = imgui.slider_int("Volume", volume, 0, 100)
```

### `imgui.slider_float`

Floating-point slider.

#### Inputs

- `label` (`str`)
- `value` (`float`)
- `min_value` (`float`)
- `max_value` (`float`)

#### Outputs

- `changed` (`bool`)
- `value` (`float`)

#### Example

```python
changed, opacity = imgui.slider_float("Opacity", opacity, 0.0, 1.0)
```

### `imgui.progress_bar`

Draws a progress bar from a normalized float value.

#### Inputs

- `fraction` (`float`): progress between `0.0` and `1.0`
- optional `size`/overlay arguments depending on binding version

#### Outputs

- None

#### Example

```python
imgui.text("Progress:")
imgui.progress_bar(progress)
```

### `imgui.combo`

Drop-down list for selecting one option.

#### Inputs

- `label` (`str`)
- `current_item` (`int`): selected index
- `items` (`list[str]`): available options

#### Outputs

- `changed` (`bool`)
- `current_item` (`int`)

#### Example

```python
changed, selected = imgui.combo(
    "Mode",
    selected,
    ["Option 1", "Option 2", "Option 3"]
)
```

### `imgui.color_edit3`

RGB color editor.

#### Inputs

- `label` (`str`)
- `r` (`float`)
- `g` (`float`)
- `b` (`float`)

#### Outputs

- `changed` (`bool`)
- color components, usually returned as updated values or a color tuple/list depending on binding version

#### Example

```python
changed, color = imgui.color_edit3("Color picker", color[0], color[1], color[2])
```

## 5. Layout and Container Widgets

### `imgui.begin_child` / `imgui.end_child`

Creates a child region inside the current window. This is useful for scrollable panels, grouped content, or nested layouts.

#### Inputs

- `label` (`str`)
- optional sizing and border arguments

#### Outputs

- `bool` from `begin_child`, which indicates whether the child region is visible and should be populated

#### Example

```python
if imgui.begin_child("LogArea", border=True, height=120):
    for line in logs:
        imgui.text(line)
    imgui.end_child()
```

### `imgui.tree_node` / `imgui.tree_pop`

Creates a collapsible tree section.

#### Inputs

- `label` (`str`)

#### Outputs

- `bool`: `True` when the node is open

#### Example

```python
if imgui.tree_node("Settings"):
    imgui.text("Advanced options")
    if imgui.tree_node("Nested group"):
        imgui.text("Nested content")
        imgui.tree_pop()
    imgui.tree_pop()
```

### `imgui.columns` / `imgui.next_column`

Splits the current area into multiple columns. This is useful for simple table-like layouts.

#### Inputs

- `columns_count` (`int`)
- optional identifier and border arguments

#### Outputs

- None

#### Example

```python
imgui.columns(3, "##stats", border=True)

imgui.text("FPS")
imgui.next_column()
imgui.text("120")
imgui.next_column()
imgui.text("Frame time")
imgui.next_column()
imgui.text("8.3 ms")

imgui.columns(1)
```

### `imgui.is_item_hovered` + `imgui.set_tooltip`

Adds contextual help when the mouse hovers over a widget.

#### Inputs

- `is_item_hovered()` takes no arguments
- `set_tooltip(text)` takes tooltip text

#### Outputs

- `is_item_hovered()`: `bool`
- `set_tooltip()`: none

#### Example

```python
if imgui.button("Help"):
    print("Help clicked")

if imgui.is_item_hovered():
    imgui.set_tooltip("Click to open the help page")
```

## 6. Multiple Windows

Use `Window` when you want separate ImGui panels that can be opened and closed independently.

### Example

```python
from ara_imgui import App, Window, imgui

app = App("Multiple Windows")

def main_ui():
    imgui.text("Main window")
    if imgui.button("Open extra window"):
        app.add_window(extra_window)

def extra_ui(window):
    imgui.text("This is a detachable window")
    _, window.value = imgui.slider_int("Value", window.value, 0, 100)

extra_window = Window("Extra Window", frame_ui=extra_ui)
extra_window.value = 50

app.run(main_ui)
```

## 7. Practical Example

The script below combines several widgets from `examples/widget_examples.py` into one small UI.

```python
from ara_imgui import App, imgui

app = App("Widget Demo", 500, 800)

enabled = True
choice = 0
name = "Michail"
count = 50
ratio = 0.5
color = [1.0, 0.5, 0.0]

def gui():
    global enabled, choice, name, count, ratio, color

    imgui.text("Widget showcase")
    imgui.separator()

    changed, enabled = imgui.checkbox("Enabled", enabled)
    changed, name = imgui.input_text("Name", name)
    changed, count = imgui.slider_int("Count", count, 0, 100)
    changed, ratio = imgui.slider_float("Ratio", ratio, 0.0, 1.0)
    changed, color = imgui.color_edit3("Color", color[0], color[1], color[2])

    if imgui.button("Submit"):
        print(name, count, ratio, color)

app.run(gui)
```

## 8. Reference Examples

Useful files in `examples/`:

- `hello_world.py` - minimal app with text and a button
- `basic_window.py` - text input and basic state updates
- `widget_examples.py` - most of the widgets shown on this page
- `multiple_window.py` - multiple `Window` instances
- `custom_font.py` - theme and font setup

## 9. Notes

- All UI code runs inside the `render` callback passed to `app.run()`
- Keep mutable widget state in variables that persist between frames
- Use `app.add_window(window)` to open a secondary window from the main UI
- For unsupported or advanced Dear ImGui features, access the underlying `imgui` module directly

# Ara_imgui

**Ara_imgui** is a lightweight and easy-to-use wrapper around [Dear ImGui](https://github.com/ocornut/imgui) using Python and GLFW. It simplifies GUI application development with ImGui by providing a convenient interface for managing windows, fonts, and application lifecycle.

## Features

- Simple ImGui app launch with a single `run` function
- Support various themes
- System or custom font loading, including Cyrillic support
- Value widgets return the new value directly; use `imgui.is_item_changed()` to react to edits
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

### Custom fonts and themes

```python
from ara_imgui import App, imgui

font_path = R"C:\Windows\Fonts\Arial.ttf"

app = App("Font Example")
app.apply_theme("cherry")
app.load_font(font_path, font_size=20)

def gui():
    imgui.text("Sample text with custom font")

app.run(gui)
```

## Examples

See the [`examples/`](./examples) folder:

* `hello_world.py` — Basic "Hello, world!" with a button.
* `basic_window.py` — Simple window with input field.
* `custom_font.py` — Font and multilingual text rendering.
* `multiple_window.py` — GUI with multiple ImGui windows.

## Dependencies

* `imgui`
* `glfw`
* `imgui_bundle`

## License

MIT License. Free to use and modify.
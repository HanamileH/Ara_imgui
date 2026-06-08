# Ara_imgui

**Ara_imgui** is a lightweight and easy-to-use wrapper around [Dear ImGui](https://github.com/ocornut/imgui) using Python and GLFW. It simplifies GUI application development with ImGui by providing a convenient interface for managing windows, fonts, and application lifecycle.

This library is designed to quickly create GUI applications using Dear ImGui in Python using a minimum amount of boiler code and focusing on simplicity and ease of use.

## Features

- Simple ImGui app launch with a single `run` function
- Support various themes
- System or custom font loading
- Ready-to-run examples included in the `examples` folder

## Installation

```bash
pip install ara_imgui
```

> ⚠️ Make sure you have Python 3.8+ and OpenGL support (e.g., via GPU drivers on Windows).

Check the successful installation using this minimal code example:

```python
from ara_imgui import App, imgui

app = App("Test App")

def gui():
    imgui.text("Hello, ImGui!")
    
app.run(gui)
```

## Quick Start
1. Create an `App` instance with a window title.
2. Define a GUI function that uses ImGui commands to build your interface.
3. Call `app.run(gui)` to start the application.

Use this template to create your own ImGui applications by adding your interface elements to the `gui` function. You can use all the features of Dear ImGui to create complex and interactive interfaces.

```python
from ara_imgui import App, imgui

app = App("Your app title", width=800, height=600)  # Optional: set window size

def gui():
    # Add your GUI elements here
    # See 'widgets' section in the documentation for available ImGui elements


def update():
    # Optional: add any per-frame logic here (e.g., updating state, handling input)
    pass


def terminate():
    # Optional: add any cleanup logic here (e.g., saving state, releasing resources)
    pass


if __name__ == "__main__":
    app.load_font("path/to/your/font.ttf", size=16)  # Optional: load a custom font
    app.apply_theme("cherry")  # Optional: apply a theme (see documentation for available themes)
    app.run(gui, update=update, terminate=terminate)
```

## Dependencies

This library depends on the following packages:
* `imgui`
* `glfw`
* `imgui_bundle`

## License

MIT License. Free to use and modify.
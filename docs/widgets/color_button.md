# imgui.color_button

## Description

Draws a colored rectangle that behaves like a button. It is commonly used to
open a color picker or to show the color currently assigned to an object.

The first argument is an ID used by ImGui, not visible text. The visible part
is the color itself.

## Syntax

```py
clicked = imgui.color_button(desc_id, col, flags=0, size=None)
```

## Parameters

- **desc_id** – (str) ID of the swatch. Supports `##` IDs and the `++` counter.
- **col** – (ImVec4Like) The displayed color, with components in the `0.0`–`1.0` range.
- **flags** – (int) Optional color-edit flags.
- **size** – (ImVec2Like) Optional swatch size.

## Return

- **clicked** – (bool) `True` on the frame the swatch was clicked.

## Usage example

```python
from ara_imgui import App, imgui

app = App("Color button")

def gui():
    color = imgui.color_edit3("Color", default=[1.0, 0.5, 0.0])

    if imgui.color_button("##swatch", imgui.ImVec4(*color, 1.0)):
        print("Color swatch clicked!")

app.run(gui)
```

## See also

- [Color edit](color_edit.md)
- [Color picker](color_picker.md)

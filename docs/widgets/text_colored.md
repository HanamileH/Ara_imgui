# imgui.text_colored

## Description

Draws a line of text using the given color. The color is an RGBA vector with
components in the `0.0`–`1.0` range. You can build it with `imgui.ImVec4` (or
pass a list of four floats).

The color affects only this call; it does not change the style for later text.

## Syntax

```py
imgui.text_colored(color, text)
```

## Parameters

- **color** – (ImVec4Like) RGBA color. Each component is in the `0.0`–`1.0` range.
- **text** – (str) The text to draw.

## Return

- This function does not return a value.

## Usage example

```python
from ara_imgui import App, imgui

app = App("Colored text")

def gui():
    imgui.text_colored(imgui.ImVec4(1.0, 0.0, 0.0, 1.0), "Red")
    imgui.text_colored(imgui.ImVec4(1.0, 1.0, 0.0, 1.0), "Yellow")
    imgui.text_colored(imgui.ImVec4(0.6, 0.6, 0.6, 1.0), "Gray")

app.run(gui)
```

The alpha component controls transparency. A common opaque color is
`(r, g, b, 1.0)`. See [Colors and vectors](../concepts.md#colors-and-vectors)
for a short explanation of `ImVec4`.

## See also

- [imgui.text](text.md)
- [Colors and vectors](../concepts.md#colors-and-vectors)

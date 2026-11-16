# imgui.text_disabled

## Description

Draws text using the current style's disabled color. This is the conventional
way to show an option that exists but cannot currently be used.

The function is purely visual; it does not disable anything by itself.

## Syntax

```py
imgui.text_disabled(text)
```

## Parameters

- **text** – (str) The text to draw.

## Return

- This function does not return a value.

## Usage example

```python
from ara_imgui import App, imgui

app = App("Disabled text")

def gui():
    imgui.text("Option A")
    imgui.text("Option B")
    imgui.text_disabled("Option C (unavailable)")

app.run(gui)
```

## See also

- [imgui.text](text.md)

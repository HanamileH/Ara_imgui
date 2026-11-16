# imgui.text

## Description

Draws a line of text in the current window or child region. Use it for labels,
instructions, status messages, and any other read-only content. Text does not
react to clicks and does not keep state.

If you need a value formatted into the text, format it in Python first with an
f-string or `str()`.

## Syntax

```py
imgui.text(text)
```

## Parameters

- **text** – (str) The text to draw. Non-string values should be converted with `str()` or an f-string.

## Return

- This function does not return a value.

## Usage example

```python
from ara_imgui import App, imgui

app = App("Text example")

def gui():
    imgui.text("Hello, world!")
    imgui.text(str(123))
    imgui.text(f"pi = {3.14159265:.2f}")

app.run(gui)
```

`imgui.text` only displays text. To make it clickable, use
[imgui.text_link](text_link.md). To change its color, use
[imgui.text_colored](text_colored.md).

## See also

- [Text concepts](../concepts.md#text)

# imgui.text_wrapped

## Description

Draws text and inserts line breaks automatically when the next word would not
fit in the available width. Use it for paragraphs, descriptions, and long
messages.

The text is wrapped using the current window width; the wrap position changes
when the window is resized.

## Syntax

```py
imgui.text_wrapped(text)
```

## Parameters

- **text** – (str) The text to draw. Long lines are wrapped automatically.

## Return

- This function does not return a value.

## Usage example

```python
from ara_imgui import App, imgui

app = App("Wrapped text")

def gui():
    imgui.text_wrapped(
        "This text automatically wraps when it reaches the edge of the window. "
        "Long paragraphs are much easier to read this way."
    )

app.run(gui)
```

## See also

- [imgui.text](text.md)

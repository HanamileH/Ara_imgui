# imgui.text_link

## Description

Draws text with the hyperlink style and reports whether it was clicked. The
function does not open a browser by itself; check the returned boolean and
perform the action yourself.

To open a URL automatically, use
[imgui.text_link_open_url](text_link_open_url.md).

## Syntax

```py
clicked = imgui.text_link(text)
```

## Parameters

- **text** – (str) The text to display as a link.

## Return

- **clicked** – (bool) `True` on the frame the link was clicked.

## Usage example

```python
from ara_imgui import App, imgui

app = App("Text link")

def gui():
    if imgui.text_link("Click here to learn more"):
        print("Link clicked!")

app.run(gui)
```

## See also

- [imgui.text_link_open_url](text_link_open_url.md)
- [imgui.text](text.md)

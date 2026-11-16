# imgui.text_link_open_url

## Description

Draws text with the hyperlink style and opens the given URL in the default web
browser when the user clicks it. It is a convenience wrapper around
`imgui.text_link()` and Dear ImGui's `TextLinkOpenURL`, which asks the platform
to open the URL.

The function does not return a value; use [imgui.text_link](text_link.md) if
you need to react to the click yourself.

## Syntax

```py
imgui.text_link_open_url(text, url)
```

## Parameters

- **text** – (str) The visible link text.
- **url** – (str) The URL opened in the default browser.

## Return

- This function does not return a value.

## Usage example

```python
from ara_imgui import App, imgui

app = App("Open URL links")

def gui():
    imgui.text_link_open_url("Open Google", "https://www.google.com")
    imgui.text_link_open_url("Visit GitHub", "https://github.com")
    imgui.text_link_open_url("Project repository", "https://github.com/HanamileH/Ara_imgui")

app.run(gui)
```

## See also

- [imgui.text_link](text_link.md)

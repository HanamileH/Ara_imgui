# imgui.text_link_open_url
## Description
Displays a text string styled as a clickable hyperlink that automatically opens the specified URL in the default web browser when clicked. Does not return any value.

## Syntax
```py
imgui.text_link_open_url(text, url)
```

## Parameters
- **text** – (str) Text to display as a hyperlink. Must be in string format.
- **url** – (str) The URL to open in the default web browser when the link is clicked. Must be in string format.

## Return
- **None** – This function does not return any value.

## Usage example
```py
import imgui

def gui():
    imgui.text_link_open_url("Open google", "https://www.google.com")
    imgui.text_link_open_url("Visit GitHub", "https://github.com")
    imgui.text_link_open_url("Documentation", "https://docs.example.com")
```
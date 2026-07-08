# imgui.text_link
## Description
Displays a text string styled as a clickable hyperlink. Returns `True` if the text was clicked.

## Syntax
```py
clicked = imgui.text_link(text)
```

## Parameters
- **text** – (str) Text to display as a hyperlink. Must be in string format.

## Return
- **clicked** – (bool) Returns `True` if the hyperlink was clicked, otherwise returns `False`.

## Usage example
```py
import imgui

def gui():
    if imgui.text_link("Click here to visit our website"):
        print("Hyperlink clicked!")
```
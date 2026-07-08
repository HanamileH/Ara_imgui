# imgui.text_wrapped
## Description
Displays a text string that automatically wraps to the next line when it reaches the edge of the containing window or region. Does not return any value.

## Syntax
```py
imgui.text_wrapped(text)
```

## Parameters
- **text** – (str) Text to display. Must be in string format. Line breaks will be inserted automatically based on the available width.

## Return
- **None** – This function does not return any value.

## Usage example
```py
import imgui

def gui():
    imgui.text_wrapped("This text will automatically wrap to the next line when it reaches the edge of the window.")
    imgui.text_wrapped("Long paragraphs or descriptions are ideal for this widget as they will adapt to the window size.")
```
# imgui.text_disabled
## Description
Displays a text string with a dimmed/disabled visual style, typically used to indicate inactive or unavailable options. Does not return any value.

## Syntax
```py
imgui.text_disabled(text)
```

## Parameters
- **text** – (str) Text to display. Must be in string format.

## Return
- **None** – This function does not return any value.

## Usage example
```py
from ara_imgui import App, imgui

def gui():
    imgui.text("Option A")
    imgui.text("Option B")
    imgui.text_disabled("Option C (disabled)")

app = App()
app.run(gui)
```

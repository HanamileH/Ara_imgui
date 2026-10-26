# imgui.input_text
## Description
Displays an input field for text

## Syntax
```py
text = imgui.input_text(label, text, flags)
```

## Parameters
- **label** – (str) Text to display next to the input field. Must be in string format.
- **text**  – (str) The current text value. Must be an text.
- **flags** – (int, optional) Flags to customize the behavior of the input field. See the `ImGuiInputTextFlags` (TODO).

## Return
- **text** – (str) The updated text value after user input.

## Usage example
```python
from ara_imgui import App, imgui

name = ""

def gui():
    global name

    name = imgui.input_text("Your name", name)
    imgui.text(f"Hello, {name or 'unknown'}!")

app = App()
app.run(gui)
```
# imgui.input_text_multiline
## Description
Displays an input field for text

## Syntax
```py
text = imgui.input_text_multiline(label, text, size, flags)
```

## Parameters
- **label** – (str) Text to display next to the input field. Must be in string format.
- **text**  – (str) The current text value. Must be an text.
- **size** – (ImVec2, optional) Size of the button. Must be an instance of `imgui.ImVec2`. If not specified, the button will use the default size.
- **flags** – (int, optional) Flags to customize the behavior of the input field. See the `ImGuiInputTextFlags` (TODO).

## Return
- **text** – (str) The updated text value after user input.

## Usage example
```python
from ara_imgui import App, imgui

desc = ""

def gui():
    global desc

    desc = imgui.input_text_multiline("Description", desc, imgui.ImVec2(200, 50))

app = App()
app.run(gui)
```
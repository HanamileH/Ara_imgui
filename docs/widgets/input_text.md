# imgui.input_text
## Description
Displays an input field for text

## Syntax
```py
changed, text = imgui.input_text(label, text, flags)
```

## Parameters
- **label** – (str) Text to display next to the input field. Must be in string format.
- **text**  – (str) The current text value. Must be an text.
- **flags** – (int, optional) Flags to customize the behavior of the input field. See the `ImGuiInputTextFlags` (TODO).

## Return
- **text** – (str) The updated text value after user input.
- **changed** – (bool) Returns `True` if the value was changed by the user, otherwise returns `False`.

## Usage example
```python
import imgui

desc = ""

def gui():
    global desc

    update, desc = imgui.input_text_multiline("Description", desc, imgui.ImVec2(200, 50))

    if update:
        print("Updated!")
        print(desc)
```
# imgui.button
## Description
Displays a button with the specified text. Returns `True` if the button was pressed.

## Syntax
```py
pressed = imgui.button(text, size)
```

## Parameters
- **text** – (str) Text to display on the button. Must be in string format.
- **size** – (ImVec2, optional) Size of the button. Must be an instance of `imgui.ImVec2`. If not specified, the button will use the default size.

## Return
- **pressed** – (bool) Returns `True` if the button was pressed, otherwise returns `False`.

## Usage example
```py
import imgui

def gui():
    if imgui.button("Click me!"):
        print("Button clicked!")

    if imgui.button("Custom size button", imgui.ImVec2(200, 50)):
        print("Second button clicked!")
```
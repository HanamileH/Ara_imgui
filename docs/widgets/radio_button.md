# imgui.radio_button
## Description
Displays a radio button. Radio buttons are used to select one option from a set of mutually exclusive options.

## Syntax
```py
pressed = imgui.radio_button(label, selected)
```

## Parameters
- **label** – (str) Text to display next to the radio button. Must be in string format.
- **selected** – (bool) Indicates whether the radio button is selected or not.

## Return
- **pressed** – (bool) Returns `True` if the radio button was clicked, otherwise returns `False`.

## Usage example
```python
import imgui

radio_first = 0
radio_second = 1

def gui():
    global radio_first, radio_second

    # Using Radio Buttons in a loop
    for i in range(3):
        if imgui.radio_button(f"Radio {i}", radio_first == i):
            radio_first = i

    # Using Radio Buttons with individual checks
    if imgui.radio_button("Option 1", radio_second == 0):
        radio_second = 0

    if imgui.radio_button("Option 2", radio_second == 1):
        radio_second = 1

    if imgui.radio_button("Option 3", radio_second == 2):
        radio_second = 2
```
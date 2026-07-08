# imgui.checkbox
## Description
Displays a checkbox. Checkboxes are used to toggle a binary state.

## Syntax
```py
checked, updated = imgui.checkbox(label, checked)
```

## Parameters
- **label** – (str) Text to display next to the checkbox. Must be in string format.
- **checked** – (bool) Indicates whether the checkbox is checked or not.

## Return
- **updated** – (bool) Returns `True` if the checkbox state was changed, otherwise returns `False`.
- **checked** – (bool) Returns the current state of the checkbox (checked or unchecked).

## Usage example
```py
import imgui

checkbox_foo = False
checkbox_bar = True
checkbox_baz = False

def gui():
    global checkbox_foo, checkbox_bar, checkbox_baz

    # First way (Recommended): use the index of the first value to check if the checkbox was clicked
    if imgui.checkbox("Checkbox Bar", checkbox_bar)[0]:
        checkbox_bar = not checkbox_bar

    # Second way: use two values ​​returned by the checkbox function, but do not use the second value
    checkbox_foo, _ = imgui.checkbox("Checkbox Foo", checkbox_foo)

    # Third way: Using both the value and update flag
    checkbox_baz, updated = imgui.checkbox("Checkbox Baz", checkbox_baz)

    if updated:
        print(f"Checkbox Baz state changed to: {checkbox_baz}")
```
    
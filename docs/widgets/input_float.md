# imgui.input_float
## Description
Displays an input field for floating-point values. Allows the user to input and modify a float value.

## Syntax
```py
value, changed = imgui.input_float(label, value, step, step_fast, format, flags)
```

## Parameters
- **label** – (str) Text to display next to the input field. Must be in string format.
- **value** – (float) The current float value. Must be a float.
- **step** – (float, optional) The amount to increment or decrement the value when using the step buttons. The default is 0.0, which means the step buttons will not be displayed.
- **step_fast** – (float, optional) The amount to increment or decrement the value when using the fast step buttons. Default is 0.0.
- **format** – (str, optional) The format string to display the float value. Default is "%.3f" which displays the value with three decimal places.
- **flags** – (int, optional) Flags to customize the behavior of the input field. See the `ImGuiInputTextFlags` (TODO).

## Return
- **value** – (float) The updated float value after user input.
- **changed** – (bool) Returns `True` if the value was changed by the user, otherwise returns `False`.

## Usage example
```py
import imgui

value = 0.0

def gui():
    global value

    value, changed = imgui.input_float("Input Float", value, step=0.1, step_fast=1.0, format="%.2f")

    if changed:
        print(f"Value changed to: {value}")

    imgui.text(f"Current value: {value}")
```
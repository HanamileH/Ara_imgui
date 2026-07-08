# imgui.input_int
## Description
Displays an input field for integer values. Allows the user to input and modify an integer value.

## Syntax
```py
value, changed = imgui.input_int(label, value, step, step_fast, flags)
```

## Parameters
- **label** – (str) Text to display next to the input field. Must be in string format.
- **value** – (int) The current integer value. Must be an integer.
- **step** – (int, optional) The amount to increment or decrement the value when using the step buttons. Default is 1.
- **step_fast** – (int, optional) The amount to increment or decrement the value when using the fast step buttons. Default is 100.
- **flags** – (int, optional) Flags to customize the behavior of the input field. See the `ImGuiInputTextFlags` (TODO).

## Return
- **value** – (int) The updated integer value after user input.
- **changed** – (bool) Returns `True` if the value was changed by the user, otherwise returns `False`.

## Usage example
```python
import imgui

age = 0

def gui():
    global age

    age, changed = imgui.input_int("Age", age)

    if changed:
        print(f"Age changed to: {age}")

        # We can change the values ​​manually to set the range of acceptable values
        if age < 0:
            age = 0
    
    imgui.text(f"Current age: {age}")
```
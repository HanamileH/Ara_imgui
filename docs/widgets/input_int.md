# imgui.input_int
## Description
Displays an input field for integer values. Allows the user to input and modify an integer value.

## Syntax
```py
value = imgui.input_int(label, value, step, step_fast, flags)
```

## Parameters
- **label** – (str) Text to display next to the input field. Must be in string format.
- **value** – (int) The current integer value. Must be an integer.
- **step** – (int, optional) The amount to increment or decrement the value when using the step buttons. Default is 1.
- **step_fast** – (int, optional) The amount to increment or decrement the value when using the fast step buttons. Default is 100.
- **flags** – (int, optional) Flags to customize the behavior of the input field. See the `ImGuiInputTextFlags` (TODO).

## Return
- **value** – (int) The updated integer value after user input.

## Usage example
```python
from ara_imgui import App, imgui

age = 0

def gui():
    global age

    age = imgui.input_int("Age", age)

    if imgui.is_item_changed():
        print(f"Age changed to: {age}")

        # We can change the values ​​manually to set the range of acceptable values
        if age < 0:
            age = 0
    
    imgui.text(f"Current age: {age}")

app = App()
app.run(gui)
```
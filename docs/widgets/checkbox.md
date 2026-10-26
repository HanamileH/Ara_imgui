# imgui.checkbox
## Description
Displays a checkbox. Checkboxes are used to toggle a binary state.

## Syntax
```py
checked = imgui.checkbox(label, checked)
```

## Parameters
- **label** – (str) Text to display next to the checkbox. Must be in string format.
- **checked** – (bool) Indicates whether the checkbox is checked or not.

## Return
- **checked** – (bool) Returns the current state of the checkbox (`True` or `False`).

## Usage example
```py
from ara_imgui import App, imgui

checkbox_foo = False
checkbox_bar = True

def gui():
    global checkbox_foo, checkbox_bar

    checkbox_foo = imgui.checkbox("Checkbox Foo", checkbox_foo)
    checkbox_bar = imgui.checkbox("Checkbox Bar", checkbox_bar)

app = App()
app.run(gui)
```
    
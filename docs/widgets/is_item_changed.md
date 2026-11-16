# imgui.is_item_changed

## Description

Value widgets return the new value, not the `changed` flag. To find out whether
the user edited the value, call `imgui.is_item_changed()` immediately after the
widget.

The function refers to the last submitted item, so it must be called directly
after the widget of interest. It is implemented on top of
`imgui.is_item_edited()`, which is the flag Dear ImGui sets when a widget
returns `changed == True`.

## Syntax

```py
changed = imgui.is_item_changed()
```

## Return

- **changed** – (bool) `True` if the last submitted widget changed its value on this frame.

## Usage example

```python
from ara_imgui import App, imgui

app = App("Item changed")

def gui():
    name = imgui.input_text("Name", default="")

    if imgui.is_item_changed():
        print(f"Name changed to {name!r}")

    age = imgui.input_int("Age", default=18)

    if imgui.is_item_changed():
        print(f"Age changed to {age}")

app.run(gui)
```

`is_item_changed()` works for value widgets only. Buttons and other clickable
widgets already return `True` when clicked, so they do not need this function.

## See also

- [Value memory](value_memory.md)
- [imgui.set_item_value](set_item_value.md)

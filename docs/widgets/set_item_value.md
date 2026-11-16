# imgui.set_item_value

## Description

Value widgets remember their value. `imgui.set_item_value(id, value)` changes
that remembered value without submitting a widget.

The first argument is the widget ID — the part of the label after `##` — or the
whole label. The new value is used the next time the widget is submitted without
an explicit value.

Passing `None` forgets the remembered value, so the widget falls back to its
`default=` or zero value on the next frame.

`set_item_value()` does not touch the ImGui item itself; it only changes what
the widget will use next time.

## Syntax

```py
imgui.set_item_value(id, value)
imgui.set_item_value(id, None)   # forget the remembered value
```

## Parameters

- **id** – (str) Widget ID or the whole label. For example `"Age##input_id"` or `"input_id"`.
- **value** – (Any) The new remembered value. `None` removes the remembered value.

## Return

- This function does not return a value.

## Usage example

```python
from ara_imgui import App, imgui

app = App("Set item value")

def gui():
    age = imgui.input_int("Age##input_id", default=18)

    if imgui.button("Reset age"):
        imgui.set_item_value("Age##input_id", 18)

    if imgui.button("Clear remembered age"):
        imgui.set_item_value("Age##input_id", None)

    imgui.text(f"Age: {age}")

app.run(gui)
```

`set_item_value` works for scalar and multi-value widgets. For example:

```python
imgui.set_item_value("Range", (0.25, 0.75))
```

## See also

- [Value memory](value_memory.md)
- [Labels and IDs](labels_and_ids.md)
- [imgui.is_item_changed](is_item_changed.md)

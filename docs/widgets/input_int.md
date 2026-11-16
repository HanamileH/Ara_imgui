# imgui.input_int

## Description

Displays an input field for an integer value. The updated value is returned
directly; use `imgui.is_item_changed()` to detect edits.

The value argument is optional. When it is omitted or `None`, the widget reuses
the value it returned on the previous frame. See
[State and IDs](state_and_ids.md#value-memory).

## Syntax

```py
value = imgui.input_int(label, value=None, step=1, step_fast=100, flags=0)
```

## Parameters

- **label** – (str) Text displayed next to the input field. Supports `##` IDs
  and the `++` counter.
- **value** – (int, optional) Current value. Omit it or pass `None` to reuse the
  previous value.
- **step** – (int, optional) Amount changed by the step buttons. Default is `1`.
- **step_fast** – (int, optional) Amount changed by the fast step buttons.
  Default is `100`.
- **flags** – (int, optional) `InputTextFlags` value.
- **default** – (int, keyword-only) Value for the first frame, when no value is
  remembered yet.

## Return

- **value** – (int) The updated integer value.

## Usage example

```python
from ara_imgui import App, imgui

def gui():
    age = imgui.input_int("Age", default=18)

    if imgui.is_item_changed():
        print(f"Age changed to: {age}")

    # Change the remembered value from code if needed.
    if imgui.button("Reset age"):
        imgui.set_item_value("Age", 18)

    imgui.text(f"Current age: {age}")

app = App()
app.run(gui)
```

For 2/3/4-component integer inputs, drag fields, and sliders, see the
[integer widget table](value_widgets.md#integers).

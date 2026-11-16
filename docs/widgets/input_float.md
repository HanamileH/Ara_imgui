# imgui.input_float

## Description

Displays an input field for a floating-point value. The updated value is
returned directly; use `imgui.is_item_changed()` to detect edits.

The value argument is optional. When it is omitted or `None`, the widget reuses
the value it returned on the previous frame. See
[State and IDs](state_and_ids.md#value-memory).

## Syntax

```py
value = imgui.input_float(label, value=None, step=0.0, step_fast=0.0, format="%.3", flags=0)
```

## Parameters

- **label** – (str) Text displayed next to the input field. Supports `##` IDs
  and the `++` counter.
- **value** – (float, optional) Current value. Omit it or pass `None` to reuse
  the previous value.
- **step** – (float, optional) Amount changed by the step buttons. Default is
  `0.0`, which hides the step buttons.
- **step_fast** – (float, optional) Amount changed by the fast step buttons.
  Default is `0.0`.
- **format** – (str, optional) Display format. Default is `"%.3"`.
- **flags** – (int, optional) `InputTextFlags` value.
- **default** – (float, keyword-only) Value for the first frame, when no value
  is remembered yet.

## Return

- **value** – (float) The updated float value.

## Usage example

```python
from ara_imgui import App, imgui

def gui():
    value = imgui.input_float(
        "Threshold",
        default=0.5,
        step=0.1,
        step_fast=1.0,
        format="%.2f",
    )
    imgui.text(f"Current value: {value}")

app = App()
app.run(gui)
```

For 2/3/4-component inputs, drag fields, sliders, angles, and vertical sliders,
see the [float widget table](value_widgets.md#floats).

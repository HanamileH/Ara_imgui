# Integer inputs

`imgui.input_int` edits one integer. The `2`, `3`, and `4` variants edit a list
of that many integers and return a new list.

## Description

All integer inputs are **value widgets**: they return the new value directly.
The value argument is optional; omit it or pass `None` to reuse the previous
value. See [Value memory](../concepts.md#value-memory).

- `input_int` edits a single `int`.
- `input_int2`, `input_int3`, and `input_int4` edit 2, 3, or 4 integers and
  return a list.

The step buttons are controlled by `step` and `step_fast`. A step of `0` hides
the fast step buttons.

## Syntax

```py
value = imgui.input_int(label, value=None, step=1, step_fast=100, flags=0)
values = imgui.input_int2(label, value=None, flags=0)
values = imgui.input_int3(label, value=None, flags=0)
values = imgui.input_int4(label, value=None, flags=0)
```

## Variants

| Function | Returns | Description |
|----------|---------|-------------|
| `imgui.input_int` | `int` | One integer. |
| `imgui.input_int2` | `list[int]` | Two integers. |
| `imgui.input_int3` | `list[int]` | Three integers. |
| `imgui.input_int4` | `list[int]` | Four integers. |

## Parameters

- **label** – (str) Visible label. Supports `##` IDs and the `++` counter.
- **value** – (int / list[int], optional) Current value. Omit it or pass `None` to reuse the previous value.
- **step** – (int) Amount added or removed by the step buttons. Default is `1`.
- **step_fast** – (int) Amount added or removed by the fast step buttons. Default is `100`.
- **flags** – (int) Optional `InputTextFlags`.
- **default** – (int / list[int]) Keyword-only value for the first frame.

## Return

- **value** – (int / list[int]) The new integer value or list of values.

## Usage example

```python
from ara_imgui import App, imgui

app = App("Integer inputs")

def gui():
    age = imgui.input_int("Age", default=18)
    position = imgui.input_int2("Position", default=[0, 0])

    imgui.text(f"Age: {age}")
    imgui.text(f"Position: {position[0]}, {position[1]}")

app.run(gui)
```

Use the drag widgets when the user should be able to change the value by
dragging, and sliders when the value has a fixed range. See
[Drag integers](drag_int.md) and [Integer sliders](slider_int.md).

## See also

- [Drag integers](drag_int.md)
- [Integer sliders](slider_int.md)
- [Value memory](../concepts.md#value-memory)

# Drag integer widgets

Drag widgets change their value when the user drags the mouse over them. Hold
Ctrl (or Cmd) while clicking to type a value directly.

`drag_int` edits one integer, `drag_int2/3/4` edit several, and
`drag_int_range2` edits the two ends of a range.

## Description

All drag widgets are **value widgets**: they return the new value directly.
The value argument is optional; omit it or pass `None` to reuse the previous
value.

`v_speed` controls how many pixels the mouse must move to change the value.
`v_min` and `v_max` limit the allowed range. The range widget returns a tuple
`(current_min, current_max)`.

## Syntax

```py
value = imgui.drag_int(label, value=None, v_speed=1.0, v_min=0, v_max=0, format="%d", flags=0)
values = imgui.drag_int2(label, value=None, v_speed=1.0, v_min=0, v_max=0, format="%d", flags=0)
values = imgui.drag_int3(label, value=None, v_speed=1.0, v_min=0, v_max=0, format="%d", flags=0)
values = imgui.drag_int4(label, value=None, v_speed=1.0, v_min=0, v_max=0, format="%d", flags=0)
low, high = imgui.drag_int_range2(label, low=None, high=None, v_speed=1.0, v_min=0, v_max=0, format="%d", format_max=None, flags=0)
```

## Variants

| Function | Returns | Description |
|----------|---------|-------------|
| `imgui.drag_int` | `int` | One integer. |
| `imgui.drag_int2` | `list[int]` | Two integers. |
| `imgui.drag_int3` | `list[int]` | Three integers. |
| `imgui.drag_int4` | `list[int]` | Four integers. |
| `imgui.drag_int_range2` | `tuple[int, int]` | Two ends of a range. |

## Parameters

- **label** – (str) Visible label. Supports `##` IDs and the `++` counter.
- **value** – (int / list[int], optional) Current value. Omit it or pass `None` to reuse the previous value.
- **low, high** – (int, optional) Current range ends for `drag_int_range2`.
- **v_speed** – (float) Mouse speed: pixels needed to change the value. Default is `1.0`.
- **v_min, v_max** – (int) Optional limits. When `v_min >= v_max`, no limit is applied.
- **format** – (str) Display format. Default is `"%d"`.
- **format_max** – (str, optional) Format for the upper handle of `drag_int_range2`.
- **flags** – (int) Optional `SliderFlags`.
- **default** – (int / tuple[int, int]) Keyword-only value for the first frame.

## Return

- **value** – (int / list[int] / tuple[int, int]) The new value, list of values, or range.

## Usage example

```python
from ara_imgui import App, imgui

app = App("Drag integers")

def gui():
    count = imgui.drag_int("Count", default=5, v_min=0, v_max=100)
    range_low, range_high = imgui.drag_int_range2(
        "Range",
        default=(10, 20),
        v_min=0,
        v_max=100,
    )

    imgui.text(f"Count: {count}")
    imgui.text(f"Range: {range_low}..{range_high}")

app.run(gui)
```

## See also

- [Integer inputs](input_int.md)
- [Integer sliders](slider_int.md)

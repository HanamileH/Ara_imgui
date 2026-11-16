# Drag float widgets

Drag widgets change their value when the user drags the mouse over them. Hold
Ctrl (or Cmd) while clicking to type a value directly.

`drag_float` edits one float, `drag_float2/3/4` edit several, and
`drag_float_range2` edits the two ends of a range.

## Description

All drag widgets are **value widgets**: they return the new value directly.
The value argument is optional; omit it or pass `None` to reuse the previous
value.

`v_speed` controls how many pixels the mouse must move to change the value.
`v_min` and `v_max` limit the allowed range. The range widget returns a tuple
`(current_min, current_max)`.

## Syntax

```py
value = imgui.drag_float(label, value=None, v_speed=1.0, v_min=0.0, v_max=0.0, format="%.3", flags=0)
values = imgui.drag_float2(label, value=None, v_speed=1.0, v_min=0.0, v_max=0.0, format="%.3", flags=0)
values = imgui.drag_float3(label, value=None, v_speed=1.0, v_min=0.0, v_max=0.0, format="%.3", flags=0)
values = imgui.drag_float4(label, value=None, v_speed=1.0, v_min=0.0, v_max=0.0, format="%.3", flags=0)
low, high = imgui.drag_float_range2(label, low=None, high=None, v_speed=1.0, v_min=0.0, v_max=0.0, format="%.3", format_max=None, flags=0)
```

## Variants

| Function | Returns | Description |
|----------|---------|-------------|
| `imgui.drag_float` | `float` | One float. |
| `imgui.drag_float2` | `list[float]` | Two floats. |
| `imgui.drag_float3` | `list[float]` | Three floats. |
| `imgui.drag_float4` | `list[float]` | Four floats. |
| `imgui.drag_float_range2` | `tuple[float, float]` | Two ends of a range. |

## Parameters

- **label** – (str) Visible label. Supports `##` IDs and the `++` counter.
- **value** – (float / list[float], optional) Current value. Omit it or pass `None` to reuse the previous value.
- **low, high** – (float, optional) Current range ends for `drag_float_range2`.
- **v_speed** – (float) Mouse speed: pixels needed to change the value. Default is `1.0`.
- **v_min, v_max** – (float) Optional limits. When `v_min >= v_max`, no limit is applied.
- **format** – (str) Display format. Default is `"%.3"`.
- **format_max** – (str, optional) Format for the upper handle of `drag_float_range2`.
- **flags** – (int) Optional `SliderFlags`.
- **default** – (float / tuple[float, float]) Keyword-only value for the first frame.

## Return

- **value** – (float / list[float] / tuple[float, float]) The new value, list of values, or range.

## Usage example

```python
from ara_imgui import App, imgui

app = App("Drag floats")

def gui():
    speed = imgui.drag_float("Speed", default=1.0, v_speed=0.05, v_min=0.0, v_max=10.0)
    range_low, range_high = imgui.drag_float_range2(
        "Exposure range",
        default=(0.2, 0.8),
        v_min=0.0,
        v_max=1.0,
    )

    imgui.text(f"Speed: {speed:.2f}")
    imgui.text(f"Range: {range_low:.2f}..{range_high:.2f}")

app.run(gui)
```

## See also

- [Float inputs](input_float.md)
- [Float sliders](slider_float.md)

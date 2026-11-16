# Float inputs

`imgui.input_float` edits one floating-point number, while `input_float2`,
`input_float3`, and `input_float4` edit 2, 3, or 4 floats. `input_double` edits
a double-precision value.

## Description

All of these widgets are **value widgets** and return the new value directly.
The value argument is optional: omit it or pass `None` to reuse the previous
value.

The `format` string controls how the number is displayed. For example, `"%.2f"`
shows two digits after the decimal point.

## Syntax

```py
value = imgui.input_float(label, value=None, step=0.0, step_fast=0.0, format="%.3", flags=0)
values = imgui.input_float2(label, value=None, format="%.3", flags=0)
values = imgui.input_float3(label, value=None, format="%.3", flags=0)
values = imgui.input_float4(label, value=None, format="%.3", flags=0)
value = imgui.input_double(label, value=None, step=0.0, step_fast=0.0, format="%.6", flags=0)
```

## Variants

| Function | Returns | Description |
|----------|---------|-------------|
| `imgui.input_float` | `float` | One float. |
| `imgui.input_float2` | `list[float] / ImVec2` | Two floats. |
| `imgui.input_float3` | `list[float]` | Three floats. |
| `imgui.input_float4` | `list[float] / ImVec4` | Four floats. |
| `imgui.input_double` | `float` | One double-precision value. |

## Parameters

- **label** – (str) Visible label. Supports `##` IDs and the `++` counter.
- **value** – (float / list[float], optional) Current value. Omit it or pass `None` to reuse the previous value.
- **step** – (float) Amount changed by the step buttons. `0.0` hides them.
- **step_fast** – (float) Amount changed by the fast step buttons.
- **format** – (str) Display format, for example `"%.3"` or `"%.2f"`.
- **flags** – (int) Optional `InputTextFlags`.
- **default** – (float / list[float]) Keyword-only value for the first frame.

## Return

- **value** – (float / list[float]) The new value or list of values.

## Usage example

```python
from ara_imgui import App, imgui

app = App("Float inputs")

def gui():
    threshold = imgui.input_float("Threshold", default=0.5, format="%.2f")
    offset = imgui.input_float2("Offset", default=[0.0, 0.0])

    imgui.text(f"Threshold: {threshold:.2f}")
    imgui.text(f"Offset: {offset[0]:.2f}, {offset[1]:.2f}")

app.run(gui)
```

## See also

- [Drag floats](drag_float.md)
- [Float sliders](slider_float.md)
- [Value memory](../concepts.md#value-memory)

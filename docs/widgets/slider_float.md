# Float sliders

Float sliders change a value inside a fixed range by dragging a handle.
`slider_angle` is a specialized slider for angles, and `v_slider_float` is the
vertical variant.

## Description

`slider_float` edits one float, `slider_float2/3/4` edit several,
`slider_angle` edits an angle in radians while showing degrees, and
`v_slider_float` is a vertical slider.

All sliders are **value widgets** and return the new value directly. The value
argument is optional, but `v_min` and `v_max` are always required. When the
value is omitted, pass the limits as keyword arguments:

```python
value = imgui.slider_float("Volume", v_min=0.0, v_max=1.0, default=0.5)
```

## Syntax

```py
value = imgui.slider_float(label, value=None, v_min=..., v_max=..., format="%.3", flags=0)
values = imgui.slider_float2(label, value=None, v_min=..., v_max=..., format="%.3", flags=0)
values = imgui.slider_float3(label, value=None, v_min=..., v_max=..., format="%.3", flags=0)
values = imgui.slider_float4(label, value=None, v_min=..., v_max=..., format="%.3", flags=0)
radians = imgui.slider_angle(label, value=None, v_degrees_min=-360.0, v_degrees_max=360.0, format="%.0 deg", flags=0)
value = imgui.v_slider_float(label, size, value=None, v_min=..., v_max=..., format="%.3", flags=0)
```

## Variants

| Function | Returns | Description |
|----------|---------|-------------|
| `imgui.slider_float` | `float` | One float. |
| `imgui.slider_float2` | `list[float] / ImVec2` | Two floats. |
| `imgui.slider_float3` | `list[float]` | Three floats. |
| `imgui.slider_float4` | `list[float] / ImVec4` | Four floats. |
| `imgui.slider_angle` | `float` | Angle in radians, displayed in degrees. |
| `imgui.v_slider_float` | `float` | Vertical float slider. |

## Parameters

- **label** – (str) Visible label. Supports `##` IDs and the `++` counter.
- **size** – (ImVec2Like) Size of a vertical slider.
- **value** – (float / list[float], optional) Current value. Omit it to reuse the previous value.
- **v_min, v_max** – (float) Required slider limits for the regular float sliders.
- **v_degrees_min, v_degrees_max** – (float) Angle limits in degrees for `slider_angle`.
- **format** – (str) Display format. Default is `"%.3"` for sliders and `"%.0 deg"` for angles.
- **flags** – (int) Optional `SliderFlags`.
- **default** – (float / list[float]) Keyword-only value for the first frame.

## Return

- **value** – (float / list[float]) The new float value or list of values.

## Usage example

```python
from ara_imgui import App, imgui

app = App("Float sliders")

def gui():
    volume = imgui.slider_float("Volume", v_min=0.0, v_max=1.0, default=0.5)
    color = imgui.slider_float3("Color", v_min=0.0, v_max=1.0, default=[1.0, 0.5, 0.0])
    angle = imgui.slider_angle("Angle", default=0.0)

    imgui.text(f"Volume: {volume:.2f}")
    imgui.text(f"Color: {color[0]:.2f}, {color[1]:.2f}, {color[2]:.2f}")
    imgui.text(f"Angle: {angle:.2f} rad")

app.run(gui)
```

## See also

- [Float inputs](input_float.md)
- [Drag floats](drag_float.md)

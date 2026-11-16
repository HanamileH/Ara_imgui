# Integer sliders

Sliders change a value inside a fixed range by dragging a handle. Unlike drag
widgets, a slider always has a visible minimum and maximum.

## Description

`slider_int` edits one integer, `slider_int2/3/4` edit several, and
`v_slider_int` is a vertical slider.

All sliders are **value widgets** and return the new value directly. The value
argument is optional, but `v_min` and `v_max` are always required. When the
value is omitted, pass the limits as keyword arguments so they are not
mistaken for the value:

```python
value = imgui.slider_int("Volume", v_min=0, v_max=100, default=50)
```

## Syntax

```py
value = imgui.slider_int(label, value=None, v_min=..., v_max=..., format="%d", flags=0)
values = imgui.slider_int2(label, value=None, v_min=..., v_max=..., format="%d", flags=0)
values = imgui.slider_int3(label, value=None, v_min=..., v_max=..., format="%d", flags=0)
values = imgui.slider_int4(label, value=None, v_min=..., v_max=..., format="%d", flags=0)
value = imgui.v_slider_int(label, size, value=None, v_min=..., v_max=..., format="%d", flags=0)
```

## Variants

| Function | Returns | Description |
|----------|---------|-------------|
| `imgui.slider_int` | `int` | One integer. |
| `imgui.slider_int2` | `list[int]` | Two integers. |
| `imgui.slider_int3` | `list[int]` | Three integers. |
| `imgui.slider_int4` | `list[int]` | Four integers. |
| `imgui.v_slider_int` | `int` | Vertical integer slider. |

## Parameters

- **label** – (str) Visible label. Supports `##` IDs and the `++` counter.
- **size** – (ImVec2Like) Size of a vertical slider.
- **value** – (int / list[int], optional) Current value. Omit it to reuse the previous value.
- **v_min, v_max** – (int) Required slider limits.
- **format** – (str) Display format. Default is `"%d"`.
- **flags** – (int) Optional `SliderFlags`.
- **default** – (int / list[int]) Keyword-only value for the first frame.

## Return

- **value** – (int / list[int]) The new integer value or list of values.

## Usage example

```python
from ara_imgui import App, imgui

app = App("Integer sliders")

def gui():
    volume = imgui.slider_int("Volume", v_min=0, v_max=100, default=50)
    size = imgui.slider_int2("Size", v_min=0, v_max=1000, default=[320, 240])

    imgui.text(f"Volume: {volume}")
    imgui.text(f"Size: {size[0]} x {size[1]}")

app.run(gui)
```

## See also

- [Integer inputs](input_int.md)
- [Drag integers](drag_int.md)

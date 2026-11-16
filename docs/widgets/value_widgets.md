# Value widgets

Value widgets are the input widgets whose Python binding returns
`(changed, value)`. Ara_imgui strips the `changed` flag and returns the value
itself:

```python
name = imgui.input_text("Name", "Michail")   # "Michail", not (False, "Michail")
```

Use [`imgui.is_item_changed()`](state_and_ids.md#is_item_changed) immediately
after the widget to know whether the user edited it.

## Common behavior

All widgets on this page support the same value handling:

```python
# 1. Explicit value: used for this frame and remembered.
age = imgui.input_int("Age##input_id", 25)

# 2. Omitted value or None: reuse the value returned on the previous frame.
age = imgui.input_int("Age##input_id")
age = imgui.input_int("Age##input_id", None)

# 3. First frame: use default= (or the type's zero value).
age = imgui.input_int("Age##input_id", default=18)

# 4. Change the remembered value explicitly.
imgui.set_item_value("Age##input_id", 18)
```

Every function on this page also accepts the keyword-only `default=` argument.
See [State and IDs](state_and_ids.md) for the full rules.

> **Vector widgets** (`*2`, `*3`, `*4`) return a `list` by default. The
> `ImVec2` / `ImVec4` overloads return that vector type instead.

## Integers

| Widget | Signature | Returns |
|--------|-----------|---------|
| `imgui.input_int` | `input_int(label, v=None, step=1, step_fast=100, flags=0)` | `int` |
| `imgui.input_int2` | `input_int2(label, v=None, flags=0)` | `list[int]` |
| `imgui.input_int3` | `input_int3(label, v=None, flags=0)` | `list[int]` |
| `imgui.input_int4` | `input_int4(label, v=None, flags=0)` | `list[int]` |
| `imgui.drag_int` | `drag_int(label, v=None, v_speed=1.0, v_min=0, v_max=0, format="%d", flags=0)` | `int` |
| `imgui.drag_int2` | `drag_int2(label, v=None, v_speed=1.0, v_min=0, v_max=0, format="%d", flags=0)` | `list[int]` |
| `imgui.drag_int3` | `drag_int3(label, v=None, v_speed=1.0, v_min=0, v_max=0, format="%d", flags=0)` | `list[int]` |
| `imgui.drag_int4` | `drag_int4(label, v=None, v_speed=1.0, v_min=0, v_max=0, format="%d", flags=0)` | `list[int]` |
| `imgui.drag_int_range2` | `drag_int_range2(label, v_current_min=None, v_current_max=None, v_speed=1.0, v_min=0, v_max=0, format="%d", format_max=None, flags=0)` | `tuple[int, int]` |
| `imgui.slider_int` | `slider_int(label, v=None, v_min=..., v_max=..., format="%d", flags=0)` | `int` |
| `imgui.slider_int2` | `slider_int2(label, v=None, v_min=..., v_max=..., format="%d", flags=0)` | `list[int]` |
| `imgui.slider_int3` | `slider_int3(label, v=None, v_min=..., v_max=..., format="%d", flags=0)` | `list[int]` |
| `imgui.slider_int4` | `slider_int4(label, v=None, v_min=..., v_max=..., format="%d", flags=0)` | `list[int]` |
| `imgui.v_slider_int` | `v_slider_int(label, size=..., v=None, v_min=..., v_max=..., format="%d", flags=0)` | `int` |

For sliders, `v_min` and `v_max` are required. When the value is omitted, pass
them as keyword arguments so they are not mistaken for the value:

```python
value = imgui.slider_int("Volume", v_min=0, v_max=100, default=50)
```

## Floats

| Widget | Signature | Returns |
|--------|-----------|---------|
| `imgui.input_float` | `input_float(label, v=None, step=0.0, step_fast=0.0, format="%.3", flags=0)` | `float` |
| `imgui.input_float2` | `input_float2(label, v=None, format="%.3", flags=0)` | `list[float]` / `ImVec2` |
| `imgui.input_float3` | `input_float3(label, v=None, format="%.3", flags=0)` | `list[float]` |
| `imgui.input_float4` | `input_float4(label, v=None, format="%.3", flags=0)` | `list[float]` / `ImVec4` |
| `imgui.input_double` | `input_double(label, v=None, step=0.0, step_fast=0.0, format="%.6", flags=0)` | `float` |
| `imgui.drag_float` | `drag_float(label, v=None, v_speed=1.0, v_min=0.0, v_max=0.0, format="%.3", flags=0)` | `float` |
| `imgui.drag_float2` | `drag_float2(label, v=None, v_speed=1.0, v_min=0.0, v_max=0.0, format="%.3", flags=0)` | `list[float]` |
| `imgui.drag_float3` | `drag_float3(label, v=None, v_speed=1.0, v_min=0.0, v_max=0.0, format="%.3", flags=0)` | `list[float]` |
| `imgui.drag_float4` | `drag_float4(label, v=None, v_speed=1.0, v_min=0.0, v_max=0.0, format="%.3", flags=0)` | `list[float]` |
| `imgui.drag_float_range2` | `drag_float_range2(label, v_current_min=None, v_current_max=None, v_speed=1.0, v_min=0.0, v_max=0.0, format="%.3", format_max=None, flags=0)` | `tuple[float, float]` |
| `imgui.slider_float` | `slider_float(label, v=None, v_min=..., v_max=..., format="%.3", flags=0)` | `float` |
| `imgui.slider_float2` | `slider_float2(label, v=None, v_min=..., v_max=..., format="%.3", flags=0)` | `list[float]` / `ImVec2` |
| `imgui.slider_float3` | `slider_float3(label, v=None, v_min=..., v_max=..., format="%.3", flags=0)` | `list[float]` |
| `imgui.slider_float4` | `slider_float4(label, v=None, v_min=..., v_max=..., format="%.3", flags=0)` | `list[float]` / `ImVec4` |
| `imgui.slider_angle` | `slider_angle(label, v_rad=None, v_degrees_min=-360.0, v_degrees_max=360.0, format="%.0 deg", flags=0)` | `float` |
| `imgui.v_slider_float` | `v_slider_float(label, size=..., v=None, v_min=..., v_max=..., format="%.3", flags=0)` | `float` |

```python
speed = imgui.slider_float("Speed", v_min=0.0, v_max=10.0, default=5.0)
```

## Text

| Widget | Signature | Returns |
|--------|-----------|---------|
| `imgui.input_text` | `input_text(label, str=None, flags=0, callback=None, user_data=None)` | `str` |
| `imgui.input_text_multiline` | `input_text_multiline(label, str=None, size=None, flags=0, callback=None, user_data=None)` | `str` |
| `imgui.input_text_with_hint` | `input_text_with_hint(label, hint, str=None, flags=0, callback=None, user_data=None)` | `str` |

```python
name = imgui.input_text("Name")
description = imgui.input_text_multiline("Description", size=imgui.ImVec2(320, 100))
search = imgui.input_text_with_hint("Search", "type to filter")
```

Note that `input_text_with_hint` takes the hint before the value; when omitting
the value, pass the hint as the second positional argument as usual.

## Boolean inputs

| Widget | Signature | Returns |
|--------|-----------|---------|
| `imgui.checkbox` | `checkbox(label, v=None)` | `bool` |
| `imgui.checkbox_flags` | `checkbox_flags(label, flags=None, flags_value=...)` | `int` |

`checkbox_flags` has a separate required `flags_value` argument. To reuse the
remembered flags while still passing the mask, use the keyword form:

```python
flags = imgui.checkbox_flags("Options", flags_value=some_flags)
```

## Selection

| Widget | Signature | Returns |
|--------|-----------|---------|
| `imgui.combo` | `combo(label, current_item=None, items=[...], popup_max_height_in_items=-1)` | `int` |
| `imgui.combo` | `combo(label, current_item=None, items_separated_by_zeros="...", popup_max_height_in_items=-1)` | `int` |
| `imgui.list_box` | `list_box(label, current_item=None, items=[...], height_in_items=-1)` | `int` |

```python
option = imgui.combo("Option", items=["One", "Two", "Three"])
option = imgui.list_box("Option", items=["One", "Two", "Three"])
```

## Colors

| Widget | Signature | Returns |
|--------|-----------|---------|
| `imgui.color_edit3` | `color_edit3(label, col=None, flags=0)` | `list[float]` / `ImVec4` |
| `imgui.color_edit4` | `color_edit4(label, col=None, flags=0)` | `list[float]` / `ImVec4` |
| `imgui.color_picker3` | `color_picker3(label, col=None, flags=0)` | `list[float]` / `ImVec4` |
| `imgui.color_picker4` | `color_picker4(label, col=None, flags=0, ref_col=None)` | `list[float]` / `ImVec4` |

The default color is black; `color_edit4` and `color_picker4` default to
`[0.0, 0.0, 0.0, 1.0]`.

```python
color = imgui.color_edit3("Color", [1.0, 0.5, 0.0])
```

## Complete example

```python
from ara_imgui import App, imgui

app = App("Value widgets")

def gui():
    name = imgui.input_text("Name", default="Michail")
    age = imgui.input_int("Age##input_id", default=18)
    volume = imgui.slider_float("Volume", v_min=0.0, v_max=1.0, default=0.5)
    option = imgui.combo("Option", items=["One", "Two", "Three"])
    color = imgui.color_edit3("Color")

    if imgui.button("Reset age"):
        imgui.set_item_value("Age##input_id", 18)

    imgui.text(f"{name}, age {age}, volume {volume:.2f}, option {option}")

app.run(gui)
```

## Related

- [State and IDs](state_and_ids.md) — value memory, `set_item_value`, `++`
- [Cheat sheet](../cheat_sheet.md) — compact list of all widgets

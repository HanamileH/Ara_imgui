# Value memory

## Description

Every **value widget** — text inputs, number inputs, sliders, drag widgets,
combo boxes, list boxes, checkboxes, and color widgets — remembers the value it
returned on the previous frame. This is what makes the value argument optional.

There are four cases:

1. **Explicit value**: the value is used for this frame and replaces the
   remembered value.
2. **Omitted value or `None`**: the remembered value is reused.
3. **No remembered value yet**: `default=` is used, or a type-appropriate zero.
4. **`set_item_value()`**: changes the remembered value from code.

The remembered value is stored under the widget ID, which is the part of the
label after `##`. Widgets with the same ID share their value.

## Syntax

```py
# 1. Explicit value
age = imgui.input_int("Age##input_id", 25)

# 2. Reuse the previous value
age = imgui.input_int("Age##input_id")
age = imgui.input_int("Age##input_id", None)

# 3. First frame
age = imgui.input_int("Age##input_id", default=18)

# 4. Change the remembered value directly
imgui.set_item_value("Age##input_id", 21)
```

## Parameters

- **value** – (widget-specific) The explicit current value. Omit it or pass `None` to reuse the remembered value.
- **default** – (widget-specific) Keyword-only value used when nothing has been remembered yet.

## Return

- **value** – (widget-specific) The value the widget has after this frame.

## Usage example

```python
from ara_imgui import App, imgui

app = App("Value memory")

def gui():
    # No global variables: the widget remembers the text itself.
    name = imgui.input_text("Name", default="")
    age = imgui.input_int("Age##input_id", default=18)

    if imgui.button("Reset age"):
        imgui.set_item_value("Age##input_id", 18)

    imgui.text(f"{name or 'Unknown'}, age {age}")

app.run(gui)
```

### Zero values

Without a `default=`, the first frame uses:

| Widget kind | Initial value |
|-------------|---------------|
| Text | `""` |
| Integer | `0` |
| Float | `0.0` |
| Checkbox | `False` |
| Combo / list box | `0` |
| `*2`, `*3`, `*4` | a list of zeros |
| `color_edit4` / `color_picker4` | `[0.0, 0.0, 0.0, 1.0]` |

### Multi-value widgets

Range widgets remember both ends and can fill only the omitted part:

```python
low, high = imgui.drag_float_range2("Range", 0.2, 0.8)
low, high = imgui.drag_float_range2("Range", 0.4, None)  # high stays 0.8
```

## See also

- [Labels and IDs](labels_and_ids.md)
- [imgui.set_item_value](set_item_value.md)
- [imgui.is_item_changed](is_item_changed.md)

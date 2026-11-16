# State and IDs

Ara_imgui adds two conveniences on top of Dear ImGui: value widgets can
remember their value, and labels ending in `++` can generate a repeated widget
ID automatically. Both features are based on the widget ID, so it is useful to
know how IDs work.

## Widget IDs

Dear ImGui derives an ID from the label. Everything after `##` (or `###`) is
the ID and is not displayed:

```python
imgui.input_text("Name##player_name")   # displays "Name", ID is "player_name"
imgui.input_text("Name")                # displays "Name", ID is "Name"
```

Widgets with the same ID share state — including Ara_imgui's remembered value:

```python
imgui.input_text("Name##player_name", "Michail")
imgui.input_text("Player##player_name")     # the same widget
```

The ID is what `set_item_value()` and the value memory use.

## Value memory

Value widgets remember the value they returned. That makes the value argument
optional:

```python
# First frame: the remembered value does not exist yet, so "" is used.
name = imgui.input_text("Name")

# A value can be passed as usual; it overwrites the remembered value.
name = imgui.input_text("Name", "Michail")

# The next frame can omit the value again and gets the previous result.
name = imgui.input_text("Name")
```

The same works with `None`:

```python
name = imgui.input_text("Name", None)   # reuse the previous value
```

If nothing has been remembered yet, `default=` is used:

```python
age = imgui.input_int("Age##input_id", default=18)
```

Without `default=`, the widget starts from a type-appropriate zero value:
`""` for text, `0` for integers and combo indexes, `0.0` for floats,
`False` for checkboxes, and zeroed lists for `*2` / `*3` / `*4` widgets.

An explicitly passed value always wins for that frame and replaces the
remembered value:

```python
new_age = 18 if imgui.button("Reset age") else None
age = imgui.input_int("Age##input_id", new_age, default=18)
```

Multi-value widgets such as `drag_float_range2` remember both values and can
fill only the omitted part:

```python
low, high = imgui.drag_float_range2("Range", 0.2, 0.8)
low, high = imgui.drag_float_range2("Range", 0.4, None)  # high stays 0.8
```

## is_item_changed

`imgui.is_item_changed()` reports whether the last submitted widget changed
its value. Call it immediately after the widget:

```python
name = imgui.input_text("Name")
if imgui.is_item_changed():
    print(f"Name changed to {name}")
```

It is implemented on top of `imgui.is_item_edited()`, which is the flag Dear
ImGui sets when a widget returns `changed == True`.

## set_item_value

`imgui.set_item_value(id, value)` changes a remembered value without
submitting a widget. It accepts the widget ID or the whole label:

```python
imgui.set_item_value("Age##input_id", 18)
age = imgui.input_int("Age##input_id")      # 18

imgui.set_item_value("input_id", 21)        # same value memory
```

Passing `None` forgets the remembered value, so the widget falls back to
`default=` or its zero value on the next frame:

```python
imgui.set_item_value("Age##input_id", None)
age = imgui.input_int("Age##input_id", default=18)  # 18
```

`set_item_value()` does not touch the ImGui item; it only changes what the
widget will use the next time it is submitted without a value.

## Automatic widget IDs with `++`

A label ending in `++` gets a counter-based ID. The counter is per label and
restarts at zero every frame:

```python
for row in rows:
    imgui.input_text("Name++", row["name"])
    if imgui.button("Delete++"):
        ...
```

The first `Name++` becomes `Name##Name_0`, the second `Name##Name_1`, and so
on. `Delete++` has a separate counter.

The generated ID is a normal ID, so it can be used with `set_item_value()`:

```python
imgui.set_item_value("Name_0", "Default name")
```

### Escape sequence

Use `\++` at the end of a label to get a literal `++` instead of a counter.
In Python source the backslash itself must be escaped:

```python
imgui.button("C\\++")   # label is C++
```

### Warnings

Ara_imgui prints a `UserWarning` in two cases:

1. **`++` on a stateful (value) widget.** The generated ID changes with
   submission order, so remembered values can move to another row if the order
   changes.
2. **`++` together with an explicit `##` ID.** The counter is appended to the
   existing ID: `"Name##player_name++"` becomes `"Name##player_name_0"`. Do not
   mix the two ways of creating an ID.

### Caveats

> ⚠️ **`++` is not the best practice.** It relies on the submission order of
> widgets. If rows are added, removed, or reordered, IDs shift and widgets can
> pick up another row's state.

Use `++` only when the order is stable. Otherwise pass an explicit ID:

```python
for row in rows:
    imgui.input_text(f"Name##row_{row.id}", row["name"])
    if imgui.button(f"Delete##row_{row.id}"):
        ...
```

An explicit ID is stable even when rows are reordered, filtered, or loaded from
different places. Stable IDs are also required when the same visible label
appears more than once, because Dear ImGui requires unique IDs inside a window.

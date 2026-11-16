# Core concepts

This page explains the ideas shared by all Ara_imgui widgets. You do not need
to know the underlying Dear ImGui library to use them.

## Immediate mode and the frame loop

Ara_imgui builds the interface from scratch on every frame. You provide a
function that describes the window; `App.run()` calls it repeatedly:

```python
from ara_imgui import App, imgui

app = App("My app")

def gui():
    imgui.text("Hello!")
    if imgui.button("Click me"):
        print("Clicked")

app.run(gui)
```

The `gui()` function is called for every frame. There are no long-lived widget
objects: each call creates the corresponding widget for that frame. This is why
the order of calls matters, and why widgets that need a value return it back to
you.

## Text

`imgui.text("Hello")` draws a read-only string. There are variants for colored
text, dimmed text, wrapped text, and clickable links; see the
[text widgets](widgets/text.md).

Text has no ID and no state. Use it for labels, instructions, and display-only
values.

## Labels and IDs

Most interactive widgets take a **label**. The label is used for two purposes:

1. The visible text drawn next to the widget.
2. An internal **ID** that Dear ImGui uses to store focus, selection, and other
   state.

Dear ImGui hides the part of the label after `##` and uses that part as the ID:

```python
imgui.input_text("Name##player_name")   # displays "Name", ID is "player_name"
imgui.input_text("Name")                # displays "Name", ID is "Name"
```

IDs must be unique within the same window. Use an explicit ID when the visible
text repeats:

```python
for row in rows:
    imgui.input_text(f"Name##row_{row.id}", row["name"])
```

A label ending in `++` asks Ara_imgui to generate a counter-based ID for you:

```python
for row in rows:
    imgui.input_text("Name++", row["name"])
```

The first call becomes `Name##Name_0`, the second `Name##Name_1`, and so on.
The counter restarts every frame. This is convenient in loops, but it depends
on submission order. If rows can be inserted, removed, or reordered, prefer an
explicit ID. See [Labels and IDs](widgets/labels_and_ids.md) for the escape
sequence and warnings.

## Value memory

Widgets that return a value are called **value widgets**: text inputs, number
inputs, sliders, drag widgets, combo boxes, list boxes, checkboxes, and color
widgets.

A value widget remembers the value it returned on the previous frame. That lets
you omit the value argument:

```python
# Explicit value: used and remembered.
age = imgui.input_int("Age##input_id", 25)

# Omitted value or None: reuse the remembered value.
age = imgui.input_int("Age##input_id")
age = imgui.input_int("Age##input_id", None)

# First frame: use default=, or the widget's zero value.
age = imgui.input_int("Age##input_id", default=18)
```

`default=` is a keyword-only argument available on every value widget. Without
it, the first frame uses a type-appropriate zero: `""` for text, `0` for
integers and combo indexes, `0.0` for floats, `False` for checkboxes, and a
list of zeros for multi-component widgets.

Passing a value explicitly always wins for that frame and replaces the
remembered value. You can also change the remembered value directly:

```python
imgui.set_item_value("Age##input_id", 18)
```

See [Value memory](widgets/value_memory.md) and
[imgui.set_item_value](widgets/set_item_value.md) for details.

## Changes and the `changed` flag

Value widgets return the new value directly, not a `(changed, value)` tuple. To
detect edits, call `imgui.is_item_changed()` immediately after the widget:

```python
name = imgui.input_text("Name")
if imgui.is_item_changed():
    print(f"Name changed to {name}")
```

Buttons and similar widgets do not need this: they already return `True` on the
frame they are clicked. See
[imgui.is_item_changed](widgets/is_item_changed.md).

## Colors and vectors

Some widgets need more than one number. Ara_imgui accepts ordinary Python lists,
and also provides the `ImVec2` / `ImVec4` helper types:

```python
position = imgui.ImVec2(10.0, 20.0)
color = imgui.ImVec4(1.0, 0.5, 0.0, 1.0)   # red, green, blue, alpha
```

- **ImVec2** is a pair of floats, commonly used for sizes and positions.
- **ImVec4** is four floats, commonly used for RGBA colors. Color components
  are in the `0.0`–`1.0` range; the fourth component is alpha.

Lists work in the same places:

```python
color = imgui.color_edit3("Color", [1.0, 0.5, 0.0])
```

## Flags

Some widgets accept a `flags` argument: an integer bit mask that enables extra
behavior. Ara_imgui exposes named flag groups under `ara_imgui.flags`:

```python
from ara_imgui import App, flags, imgui

app = App("Flags")

def gui():
    input_flags = flags.input_text.chars_no_blank | flags.input_text.password
    password = imgui.input_text("Password", flags=input_flags)
    imgui.text(f"Length: {len(password)}")

app.run(gui)
```

Combine flags with the bitwise OR operator `|`. The default is `0`, meaning no
special behavior.

## Context managers

Some widgets have a matching `end` call. Ara_imgui provides `with`-based
versions that do the cleanup for you:

```python
with imgui.child("Log"):
    imgui.text("Child content")

with imgui.tree("Settings") as opened:
    if opened:
        imgui.text("Advanced options")

with imgui.table("People", 3, ["Name", "Age", "Sex"]):
    ...
```

- [imgui.child](widgets/child.md) manages `begin_child()` / `end_child()`.
- [imgui.tree](widgets/tree.md) manages `tree_node()` / `tree_pop()`.
- [imgui.table](widgets/table.md) manages the legacy `columns()` API.

For trees and children, the context manager is truthy only while the content is
visible/open, so expensive content can be guarded with `if`.

## Lists and tuples

Some widgets return several values:

- `*2`, `*3`, and `*4` widgets return a list of values.
- Range widgets such as `drag_float_range2` return a tuple `(low, high)`.
- `selectable`, `menu_item`, and `begin_tab_item` return tuples that include an
  action flag.

The documentation for each widget lists the exact return type.

## Where to go next

- [Cheat sheet](cheat_sheet.md) — every widget on one page
- [Widget overview](widgets/index.md) — the same catalog with short descriptions
- [Labels and IDs](widgets/labels_and_ids.md) — explicit IDs and `++` counters
- [Value memory](widgets/value_memory.md) — omitted values and `default=`

# Labels and IDs

## Description

Widgets that accept a label use it for two things: the visible text and the
internal ID that Dear ImGui uses to store state.

### Visible label and ID

Everything after `##` is part of the ID and is not displayed:

```python
imgui.input_text("Name##player_name")   # displays "Name", ID is "player_name"
imgui.input_text("Name")                # displays "Name", ID is "Name"
```

Widgets with the same ID share state, including remembered values. Use a stable
explicit ID when the visible text might repeat.

### The `++` counter

A label ending in `++` gets a per-label counter ID. The counter starts at zero
every frame:

```python
for row in rows:
    imgui.input_text("Name++", row["name"])
    if imgui.button("Delete++"):
        ...
```

The first `Name++` becomes `Name##Name_0`, the second `Name##Name_1`, and so on.
`Delete++` has its own counter.

### Escape sequence

Use `\++` at the end of a label to get a literal `++`. In Python source the
backslash must be escaped too:

```python
imgui.button("C\\++")   # label is C++
```

### Warnings

Ara_imgui prints a warning in two cases:

1. `++` is used with a stateful value widget. The generated ID changes with
   submission order, so remembered values can move to another row.
2. `++` is combined with an explicit `##` ID. The counter is appended to the
   explicit ID: `"Name##player_name++"` becomes `"Name##player_name_0"`.

### Use explicit IDs when order can change

> ⚠️ `++` is a convenience, not a best practice. If rows are inserted, removed,
> or reordered, IDs shift and widgets can pick up another row's state.

Use `++` only when the order is stable. Otherwise pass an explicit ID:

```python
for row in rows:
    imgui.input_text(f"Name##row_{row.id}", row["name"])
    if imgui.button(f"Delete##row_{row.id}"):
        ...
```

## Syntax

```py
imgui.input_text("Visible label##stable_id")
imgui.input_text("Visible label++")
imgui.button("Literal plus plus\\++")
```

## Usage example

```python
from ara_imgui import App, imgui

rows = ["First", "Second", "Third"]

app = App("Labels and IDs")

def gui():
    for index, row in enumerate(rows):
        # Stable ID: remains the same even if rows are reordered.
        imgui.input_text(f"Name##row_{index}", row)

    for index, row in enumerate(rows):
        # Counter ID: convenient, but depends on submission order.
        imgui.input_text("Note++", default="")

    imgui.text("Open the source of this example to compare both approaches.")

app.run(gui)
```

## See also

- [Value memory](value_memory.md)
- [imgui.set_item_value](set_item_value.md)

# imgui.selectable

## Description

Draws a selectable row, commonly used in lists, tables, and custom combo boxes.
The returned tuple contains two booleans: whether the row was clicked and
whether it should now be selected.

You own the selection state; `imgui.selectable` only reports what happened.

## Syntax

```py
clicked, selected = imgui.selectable(label, selected, flags=0, size=None)
```

## Parameters

- **label** – (str) Visible row text. Supports `##` IDs and the `++` counter.
- **selected** – (bool) Whether the row is currently selected.
- **flags** – (int) Optional `SelectableFlags`.
- **size** – (ImVec2Like) Optional row size.

## Return

- **clicked** – (bool) `True` when the row was clicked.
- **selected** – (bool) Whether the row is selected after the click.

## Usage example

```python
from ara_imgui import App, imgui

app = App("Selectable rows")

selected_index = 0

def gui():
    global selected_index

    for index, name in enumerate(["Alpha", "Beta", "Gamma"]):
        clicked, _ = imgui.selectable(f"{name}##row_{index}", index == selected_index)
        if clicked:
            selected_index = index

    imgui.text(f"Selected: {selected_index}")

app.run(gui)
```

When rows are generated in a loop, each row needs a unique ID. Use
`f"row##{row.id}"` or the `++` counter. See
[Labels and IDs](../concepts.md#labels-and-ids).

## See also

- [Menus](menus.md)
- [List box](list_box.md)

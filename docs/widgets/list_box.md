# List box

`imgui.list_box` is a ready-made scrollable list. `imgui.begin_list_box` lets
you build a custom list whose entries are arbitrary widgets.

## Description

The simple form takes a list of strings and returns the selected index. The
current index is optional; omit it or pass `None` to reuse the previous value.

The custom form opens a list region and lets you draw any widgets inside it.
Close it with `imgui.end_list_box()`.

## Syntax

```py
selected = imgui.list_box(label, current_item=None, items=[...], height_in_items=-1)

if imgui.begin_list_box(label, size=None):
    # custom entries
    imgui.end_list_box()
```

## Variants

| Function | Returns | Description |
|----------|---------|-------------|
| `imgui.list_box` | `int` | Scrollable list of string items. |
| `imgui.begin_list_box` | `bool` | Opens a custom list region. |

## Parameters

- **label** – (str) Visible label. Supports `##` IDs and the `++` counter.
- **current_item** – (int, optional) Selected index. Omit it or pass `None` to reuse the previous value.
- **items** – (list[str]) Strings shown in the list.
- **height_in_items** – (int) Visible rows. Default is `-1` (fit the available space).
- **size** – (ImVec2Like, optional) Size of a custom list region.
- **default** – (int) Keyword-only selected index for the first frame.

## Return

- **selected** – (int) `list_box`: index of the selected item.
- **opened** – (bool) `begin_list_box`: whether the list region is open.

## Usage example

```python
from ara_imgui import App, imgui

options = ["Red", "Green", "Blue", "Yellow"]

app = App("List box")

def gui():
    selected = imgui.list_box("Color", items=options)
    imgui.text(f"Selected: {options[selected]}")

app.run(gui)
```

### Custom list box

```python
entries = ["First", "Second", "Third"]
selected = 0

def gui():
    global selected
    if imgui.begin_list_box("Entries", imgui.ImVec2(200, 100)):
        for index, entry in enumerate(entries):
            clicked, _ = imgui.selectable(
                f"{entry}##entry_{index}",
                index == selected,
            )
            if clicked:
                selected = index
        imgui.end_list_box()
```

## See also

- [Combo box](combo.md)
- [Selectable](selectable.md)

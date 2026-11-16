# Combo box

`imgui.combo` is the ready-made dropdown. `imgui.begin_combo` lets you build a
custom dropdown whose entries are arbitrary widgets instead of plain strings.

## Description

The simple form takes a list of strings and returns the selected index. The
current index is optional; omit it or pass `None` to reuse the previous value.

The custom form opens a popup and lets you draw any widgets inside it. Use
`imgui.selectable` for the entries and call `imgui.end_combo()` when finished.

## Syntax

```py
selected = imgui.combo(label, current_item=None, items=[...], popup_max_height_in_items=-1)

if imgui.begin_combo(label, preview_value):
    # custom entries
    imgui.end_combo()
```

## Variants

| Function | Returns | Description |
|----------|---------|-------------|
| `imgui.combo` | `int` | Dropdown made of string items. |
| `imgui.begin_combo` | `bool` | Opens a custom combo popup. |

## Parameters

- **label** – (str) Visible label. Supports `##` IDs and the `++` counter.
- **current_item** – (int, optional) Selected index. Omit it or pass `None` to reuse the previous value.
- **items** – (list[str]) Strings shown in the dropdown.
- **popup_max_height_in_items** – (int) Maximum visible rows before the popup scrolls. Default is `-1`.
- **preview_value** – (str) Text shown in the closed custom combo.
- **default** – (int) Keyword-only selected index for the first frame.

## Return

- **selected** – (int) `combo`: index of the selected item.
- **opened** – (bool) `begin_combo`: whether the popup is open.

## Usage example

```python
from ara_imgui import App, imgui

options = ["Apple", "Banana", "Cherry", "Watermelon"]

app = App("Combo box")

def gui():
    selected = imgui.combo("Fruit", items=options)
    imgui.text(f"You selected: {options[selected]}")

    if imgui.button("Reset selection"):
        imgui.set_item_value("Fruit", 0)

app.run(gui)
```

### Custom combo

Use `begin_combo` when the entries need more than plain text:

```python
users = [("Anna", 25), ("Bob", 31)]
selected = 0

def gui():
    global selected
    preview = f"{users[selected][0]}, {users[selected][1]}"

    if imgui.begin_combo("User", preview):
        for index, (name, age) in enumerate(users):
            clicked, _ = imgui.selectable(
                f"{name}, {age}##user_{index}",
                index == selected,
            )
            if clicked:
                selected = index
        imgui.end_combo()

    imgui.text(f"Selected index: {selected}")
```

## See also

- [List box](list_box.md)
- [Selectable](selectable.md)

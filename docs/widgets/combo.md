# imgui.combo

## Description

Displays a combo box with a list of options and returns the index of the
selected item.

The current item argument is optional. When it is omitted or `None`, the widget
reuses the value it returned on the previous frame. See
[State and IDs](state_and_ids.md#value-memory).

## Syntax

```py
selected = imgui.combo(label, current_item=None, items=[...], popup_max_height_in_items=-1)
```

The second overload accepts a `\0`-separated string:

```py
selected = imgui.combo(label, current_item=None, items_separated_by_zeros="One\0Two\0Three\0")
```

## Parameters

- **label** – (str) Text displayed next to the combo box. Supports `##` IDs and
  the `++` counter.
- **current_item** – (int, optional) Index of the selected item. Omit it or
  pass `None` to reuse the previous value.
- **items** – (list[str]) Options to display.
- **items_separated_by_zeros** – (str) Options separated by `\0`, ending with
  `\0\0`.
- **popup_max_height_in_items** – (int, optional) Maximum number of items shown
  before the popup scrolls. Default is `-1`.
- **default** – (int, keyword-only) Selected index for the first frame.

## Return

- **selected** – (int) Index of the selected item.

## Usage example

```python
from ara_imgui import App, imgui

options = ["Apple", "Banana", "Cherry", "Watermelon"]

def gui():
    selected = imgui.combo("Fruit", items=options)
    imgui.text(f"You selected: {options[selected]}")

    if imgui.button("Reset selection"):
        imgui.set_item_value("Fruit", 0)

app = App()
app.run(gui)
```

### Example with user data

```python
from ara_imgui import App, imgui

users = [{"id": i, "name": f"User {i}", "age": i % 30 + 20} for i in range(100)]

def gui():
    selected_pos = imgui.combo(
        "Users",
        items=[f'{user["name"]} age: {user["age"]}' for user in users],
        popup_max_height_in_items=10,
    )

    imgui.text(f"Selected user id: {users[selected_pos]['id']}")

app = App()
app.run(gui)
```

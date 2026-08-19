# imgui.combo
## Description
Displays a combo box with a list of options. Allows the user to select one of the options.

## Syntax
```py
changed, selected = imgui.combo(label, selected, items, popup_max_items_in_height)
```

## Parameters
- **label** – (str) Text to display next to the combo box. Must be in string format.
- **selected** – (int) Index of the currently selected item.
- **items** – (list) List of items to display in the combo box.
- **popup_max_items_in_height** – (int, optional) Maximum number of items to display in the combo box. If the number of items exceeds this value, a scrollbar will be displayed.

## Return
- **changed** – (bool) True if the user selected a different item, False otherwise.
- **selected** – (int) Index of the currently selected item.

## Usage example
```py
import imgui

options = ["Apple", "Banana", "Cherry", "Watermelon"]
selected = 0

def gui():
    global selected

    _, selected = imgui.combo("Fruit", selected, options)

    imgui.text(f"You selected: {options[selected]}")
```

<br>

Usage example with user data:
```py
import imgui

users = [{"id": i, "name": f"User {i}", "age": i % 30 + 20} for i in range(100)]

selected_pos = 0
selected_id = users[0]['id']

def gui():
    global selected_pos, selected_id

    changed, selected_pos = imgui.combo(
        "Users",
        selected_pos,
        [f'{user["name"]} age: {user["age"]}' for user in users],
        10
    )

    if changed:
        selected_id = users[selected_pos]['id']

    imgui.text(f"Selected user id: {selected_id}")
```
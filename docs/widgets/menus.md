# Menus

Menus are hierarchical lists of commands. `begin_menu()` opens a submenu,
`menu_item()` draws one command inside it, and the matching `end_menu()` closes
the submenu.

## Description

A menu is built from three parts:

1. A menu bar, `imgui.begin_menu_bar()` / `imgui.end_menu_bar()`.
2. A submenu, `imgui.begin_menu(label)` / `imgui.end_menu()`.
3. One or more entries, `imgui.menu_item(label, shortcut, selected)`.

`menu_item()` returns `(clicked, selected)`: the first value tells you whether
the command was chosen, the second is the check-mark state. `begin_menu()`
returns whether the submenu is open, so its contents are usually guarded with
`if`.

The label of `begin_menu` supports `##` IDs and the `++` counter.

## Syntax

```py
opened = imgui.begin_menu(label, enabled=True)
clicked, selected = imgui.menu_item(label, shortcut, selected, enabled=True)
imgui.end_menu()
```

## Variants

| Function | Returns | Description |
|----------|---------|-------------|
| `imgui.begin_menu` | `bool` | Opens a submenu; returns whether it is open. |
| `imgui.menu_item` | `tuple[bool, bool]` | Draws one menu entry; returns `(clicked, selected)`. |

## Parameters

- **label** – (str) Visible menu or entry text. Supports `##` IDs and `++`.
- **enabled** – (bool) Whether the submenu or entry can be used. Default is `True`.
- **shortcut** – (str) Optional shortcut text such as `"Ctrl+O"`. It is displayed but not handled automatically.
- **selected** – (bool) Whether the entry shows a check mark.

## Return

- **opened** – (bool) `begin_menu`: whether the submenu is open.
- **clicked** – (bool) `menu_item`: whether the entry was chosen.
- **selected** – (bool) `menu_item`: the check-mark state.

## Usage example

```python
from ara_imgui import App, imgui

app = App("Menus")

def gui():
    if imgui.begin_menu_bar():
        if imgui.begin_menu("File"):
            clicked, _ = imgui.menu_item("Open", "Ctrl+O", False)
            if clicked:
                print("Open")

            clicked, _ = imgui.menu_item("Quit", "Ctrl+Q", False)
            if clicked:
                print("Quit")

            imgui.end_menu()
        imgui.end_menu_bar()

    imgui.text("Use the File menu above.")

app.run(gui)
```

`begin_menu_bar()` is not wrapped by Ara_imgui, but it is available unchanged
from `imgui_bundle` and is used exactly like in the example. The same applies to
`end_menu_bar()`.

## See also

- [Selectable](selectable.md)
- [Popups](popups.md)

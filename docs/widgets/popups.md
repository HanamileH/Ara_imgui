# Popups

Popups are temporary windows that appear above the rest of the UI. Use
`open_popup()` to request one, then `begin_popup()` or `begin_popup_modal()` to
draw it.

## Description

`imgui.open_popup(str_id)` requests that the popup with that ID opens on the
current frame or the next one.

`imgui.begin_popup(str_id)` starts a regular popup; call `imgui.end_popup()`
when finished.

`imgui.begin_popup_modal(name)` starts a modal dialog, which blocks interaction
with the rest of the application until it is closed. Its optional `p_open`
parameter adds a close button. The function returns `(visible, p_open)`.

## Syntax

```py
imgui.open_popup(str_id, popup_flags=0)
if imgui.begin_popup(str_id, flags=0):
    ...
    imgui.end_popup()

visible, p_open = imgui.begin_popup_modal(name, p_open=None, flags=0)
```

## Variants

| Function | Returns | Description |
|----------|---------|-------------|
| `imgui.open_popup` | `bool` | Requests a popup to open. |
| `imgui.begin_popup` | `bool` | Draws a regular popup. |
| `imgui.begin_popup_modal` | `tuple[bool, bool | None]` | Draws a modal dialog. |

## Parameters

- **str_id** – (str) Popup ID. Supports `##` IDs and the `++` counter.
- **name** – (str) Modal window title and ID.
- **p_open** – (bool, optional) Adds a close button to a modal.
- **popup_flags** – (int) Optional popup flags for `open_popup`.
- **flags** – (int) Optional window flags.

## Return

- **visible** – (bool) Whether the popup contents should be drawn.
- **p_open** – (bool | None) The updated close state of a modal.

## Usage example

```python
from ara_imgui import App, imgui

app = App("Popups")

def gui():
    if imgui.button("Open popup"):
        imgui.open_popup("my_popup")

    if imgui.begin_popup("my_popup"):
        imgui.text("This is a popup.")
        if imgui.button("Close"):
            imgui.close_current_popup()
        imgui.end_popup()

app.run(gui)
```

Use `imgui.close_current_popup()` to close a popup from inside it. The modal
example below also shows the returned `p_open` state:

```python
show_modal = True

def gui():
    global show_modal
    if show_modal:
        visible, show_modal = imgui.begin_popup_modal(
            "Confirm##modal", show_modal
        )
        if visible:
            imgui.text("Are you sure?")
            if imgui.button("OK"):
                show_modal = False
                imgui.close_current_popup()
            imgui.end_popup()
```

## See also

- [Window](window.md)
- [Menus](menus.md)

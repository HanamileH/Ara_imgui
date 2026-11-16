# imgui.begin / imgui.end

## Description

`imgui.begin()` starts a window and `imgui.end()` closes it. `App.run()` already
opens a full-screen main window, so most applications do not need to call
`begin()` themselves. It is useful for floating tool windows.

`begin()` returns a tuple `(visible, p_open)`. Only draw the window contents
when `visible` is `True`. The optional `p_open` parameter lets ImGui add a close
button; when the user closes the window, `p_open` becomes `False`.

The window name is also its ID and must be unique. Use `"Title##stable_id"` if
you want a different visible title.

## Syntax

```py
visible, p_open = imgui.begin(name, p_open=None, flags=0)
# ... window contents ...
imgui.end()
```

## Parameters

- **name** – (str) Window title and ID. Supports `##` IDs and the `++` counter.
- **p_open** – (bool, optional) Set to `True` to show a close button; the returned value becomes `False` when closed.
- **flags** – (int) Optional `WindowFlags`.

## Return

- **visible** – (bool) Whether the window contents should be drawn.
- **p_open** – (bool | None) The updated close state when `p_open` was passed.

## Usage example

```python
from ara_imgui import App, imgui

app = App("Own window")

show_tools = True

def gui():
    global show_tools

    if imgui.button("Toggle tools"):
        show_tools = not show_tools

    if show_tools:
        visible, _ = imgui.begin("Tools##tools_window")
        if visible:
            imgui.text("Floating tool window")
            if imgui.button("Do something"):
                print("Done")
        imgui.end()

app.run(gui)
```

## See also

- [Child window](child.md)
- [Popups](popups.md)

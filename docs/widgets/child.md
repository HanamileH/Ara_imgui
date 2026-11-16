# imgui.child

## Description

Context manager around `imgui.begin_child()` / `imgui.end_child()`. It creates
a child window region that can be independently scrolled and clipped, and calls
`end_child()` automatically. The context manager is truthy while the child is
visible, so expensive contents can be guarded with `if child:`.

## Syntax

```py
with imgui.child(str_id, size=None, child_flags=0, window_flags=0) as child:
    if child:
        # Child items
        ...
```

The raw ImGui API is also available:

```py
if imgui.begin_child(str_id, size=None, child_flags=0, window_flags=0):
    # Child items
    ...
    imgui.end_child()
```

## Parameters

- **str_id** – (str) Child window ID. It follows the normal `##` ID rules and
  supports a trailing `++` counter.
- **size** – (ImVec2, optional) Size of the child window.
- **child_flags** – (int, optional) Child window flags.
- **window_flags** – (int, optional) Window flags.

## Return

A context manager whose truth value is `True` while the child is visible. It
also exposes the **visible** attribute.

## Usage example

```py
from ara_imgui import App, imgui

def gui():
    if imgui.begin_child("Child Window", imgui.ImVec2(400, 200)):
        for _ in range(100):
            imgui.text("Too many lines")
        imgui.end_child()

    imgui.separator()

    with imgui.child("Child Window 2") as child:
        if child:
            imgui.text("This is another child window")

app = App()
app.run(gui)
```

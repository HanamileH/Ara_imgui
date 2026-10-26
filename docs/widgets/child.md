# imgui.child, imgui.begin_child and imgui.end_child
## Description
Begins a child window region that can be independently scrolled and clipped.

## Syntax
```py
with imgui.child(child_id, size, child_flags, window_flags) as child:
    if child:
        # Child items
        # ...
```

Or:

```py
if imgui.begin_child(child_id, size, child_flags, window_flags):
    # Child items
    # ...
    imgui.end_child()
```

## Parameters
- **child_id** – (str) Unique identifier for the child window.
- **size** – (ImVec2, optional) Size of the child window.
- **child_flags** – (int, optional) Flags for the child window.
- **window_flags** – (int, optional) Flags for the window.

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

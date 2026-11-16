# imgui.child

## Description

A child window is a clipped, independently scrollable region inside the current
window. It is useful for logs, lists, and any content that should not stretch
the parent window.

`imgui.child()` is a context manager: it calls `begin_child()` and
`end_child()` for you. It is truthy while the child is visible, so expensive
contents can be guarded with `if child:`.

`imgui.begin_child()` / `imgui.end_child()` are also available for the raw
ImGui style.

## Syntax

```py
with imgui.child(str_id, size=None, child_flags=0, window_flags=0) as child:
    if child:
        ...

if imgui.begin_child(str_id, size=None, child_flags=0, window_flags=0):
    ...
    imgui.end_child()
```

## Parameters

- **str_id** – (str) Child window ID. Supports `##` IDs and the `++` counter.
- **size** – (ImVec2Like, optional) Child size. Use `imgui.ImVec2(width, height)`.
- **child_flags** – (int) Optional child-window flags.
- **window_flags** – (int) Optional window flags.

## Return

- **child** – (context manager / bool) Truthy while the child is visible.

## Usage example

```python
from ara_imgui import App, imgui

app = App("Child window")

def gui():
    with imgui.child("Log", imgui.ImVec2(0, 120)) as child:
        if child:
            for index in range(20):
                imgui.text(f"Log line {index}")

    imgui.text("This text is outside the child.")

app.run(gui)
```

## See also

- [Table](table.md)
- [Trees](tree.md)

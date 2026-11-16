# Trees and collapsing headers

Trees and collapsing headers hide content behind an expandable row. The
`imgui.tree` context manager is the easiest way to use a tree node because it
calls `tree_pop()` for you.

## Description

`imgui.tree_node()` draws an expandable node and returns whether it is open.
When it is open, draw its contents and call `imgui.tree_pop()` at the end.

`imgui.tree_push()` pushes an ID onto the tree stack without drawing anything;
it is useful for grouping several nodes under one ID.

`imgui.collapsing_header()` is similar to a tree node but uses the collapsing
header style.

The `imgui.tree` context manager wraps `tree_node()` / `tree_pop()` and is
truthy only while the node is open.

## Syntax

```py
opened = imgui.tree_node(label)
imgui.tree_push(str_id)
opened = imgui.collapsing_header(label, flags=0)
imgui.tree_pop()

with imgui.tree(label) as opened:
    if opened:
        ...
```

## Variants

| Function | Returns | Description |
|----------|---------|-------------|
| `imgui.tree_node` | `bool` | Expandable tree node; call `tree_pop()` when it is open. |
| `imgui.tree_push` | `None` | Push an ID onto the tree stack. |
| `imgui.collapsing_header` | `bool` | Collapsible header. |
| `imgui.tree` | `context manager` | Wraps `tree_node` / `tree_pop`; truthy while open. |

## Parameters

- **label** – (str) Visible label. Supports `##` IDs and the `++` counter.
- **str_id** – (str) ID pushed by `tree_push`.
- **flags** – (int) Optional `TreeNodeFlags` for `collapsing_header`.

## Return

- **opened** – (bool) Whether the node or header is open.

## Usage example

```python
from ara_imgui import App, imgui

app = App("Trees")

def gui():
    with imgui.tree("Settings") as opened:
        if opened:
            imgui.text("Advanced options")

            with imgui.tree("Appearance") as child:
                if child:
                    imgui.text("Theme settings")

    imgui.separator()

    if imgui.collapsing_header("Details"):
        imgui.text("Collapsed and expanded with collapsing_header().")

app.run(gui)
```

A collapsed node must not submit its children. With the context manager, guard
the body with `if opened:`. With the raw API, call `imgui.tree_pop()` only when
`tree_node()` returned `True`.

## See also

- [Labels and IDs](../concepts.md#labels-and-ids)

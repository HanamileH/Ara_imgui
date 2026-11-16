# imgui.tree

## Description

Context manager around `imgui.tree_node()` / `imgui.tree_pop()`. `tree_pop()`
is called automatically, but only when the node is open. The context manager is
truthy exactly while the node is open, so guard its body with `if node:`.

## Syntax

```py
with imgui.tree(label) as node:
    if node:
        # Contents of the open node
        ...
```

`imgui.tree()` also supports the `tree_node` overloads:

```py
with imgui.tree(str_id, fmt) as node:
    ...

with imgui.tree(ptr_id, fmt) as node:
    ...
```

## Parameters

- **label** / **str_id** / **ptr_id** – The same first argument as
  `imgui.tree_node()`. A string label supports `##` IDs and a trailing `++`
  counter.
- **fmt** – (str, optional) Format string for the displayed label when using a
  string ID or pointer ID.

## Return

A context manager whose truth value is `True` while the node is open. It also
exposes the **expanded** attribute.

## Usage example

```py
from ara_imgui import App, imgui

def gui():
    with imgui.tree("Settings") as node:
        if node:
            imgui.text("Advanced options")

            with imgui.tree("Appearance") as child:
                if child:
                    imgui.text("Theme settings")

app = App()
app.run(gui)
```

A collapsed node must not submit its children, hence the `if node:` guard.
Repeated nodes can use the `++` counter, but prefer a stable explicit ID when
the order can change:

```py
with imgui.tree(f"Row##row_{row.id}") as node:
    ...
```

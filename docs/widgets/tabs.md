# Tabs

## Description

`imgui.begin_tab_bar()` starts a tab bar and `imgui.begin_tab_item()` adds one
tab. A tab item must be ended with `imgui.end_tab_item()` **only when it is
visible**; the tab bar itself is ended with `imgui.end_tab_bar()`.

`begin_tab_item()` returns `(visible, p_open)`. Draw the tab contents and call
`end_tab_item()` when `visible` is `True`. The optional `p_open` parameter adds
a close button to the tab.

## Syntax

```py
if imgui.begin_tab_bar(str_id, flags=0):
    visible, p_open = imgui.begin_tab_item(label, p_open=None, flags=0)
    if visible:
        ...
        imgui.end_tab_item()
    imgui.end_tab_bar()
```

## Parameters

- **str_id** – (str) Tab bar ID. Supports `##` IDs and the `++` counter.
- **label** – (str) Tab title and ID.
- **p_open** – (bool, optional) Adds a close button to the tab.
- **flags** – (int) Optional `TabBarFlags` / `TabItemFlags`.

## Return

- **visible** – (bool) Whether the tab contents should be drawn.
- **p_open** – (bool | None) The updated close state of the tab.

## Usage example

```python
from ara_imgui import App, imgui

app = App("Tabs")

def gui():
    if imgui.begin_tab_bar("settings_tabs"):
        visible, _ = imgui.begin_tab_item("General")
        if visible:
            imgui.text("General settings")
            imgui.end_tab_item()

        visible, _ = imgui.begin_tab_item("Advanced")
        if visible:
            imgui.text("Advanced settings")
            imgui.end_tab_item()

        imgui.end_tab_bar()

app.run(gui)
```

## See also

- [Window](window.md)
- [Tables](table.md)

# imgui.separator

## Description

Draws a horizontal line that separates groups of widgets. It is purely visual:
it has no label and no state.

`imgui.separator` is often used between blocks of controls and between a table
header and its rows.

## Syntax

```py
imgui.separator()
```

## Return

- This function does not return a value.

## Usage example

```python
from ara_imgui import App, imgui

app = App("Separator example")

def gui():
    imgui.text("First group")
    imgui.separator()
    imgui.text("Second group")

app.run(gui)
```

## See also

- [imgui.text](text.md)
- [Tables](table.md)

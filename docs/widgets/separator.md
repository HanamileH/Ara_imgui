# imgui.separator
## Description
Displays a horizontal separator line. Useful for separating objects into groups and also for formatting tables.

## Syntax
```py
imgui.separator()
```

## Parameters
- None

## Return
- None

## Usage example
```python
import imgui

def gui():
    imgui.text("First group")
    imgui.separator()
    imgui.text("Second group")

    # You can also use it to separate table rows
    imgui.columns(3)

    for title in ["Column A", "Column B", "Column C"]:
        imgui.text(title)
        imgui.next_column()
    
    # Separation between table header and table rows
    imgui.separator()

    for i in range(15):
            imgui.text(f"Item {i}")
            imgui.next_column()

    imgui.columns(1)
```
# imgui.text
## Description
Displays text. Nothing special.

## Syntax
```py
imgui.text(label)
```

## Parameters
- **label** – (str) Text to display. Must be in string format.

## Return
- None

## Usage example
```python
import imgui

pi = 3.14159265

def gui():
    imgui.text("Hello, world!")
    imgui.text(str(123))
    imgui.text(f"pi = {pi:.2f}")
```
# imgui.text_colored
## Description
Displays colored text. This function allows you to display text with a specified color.

## Syntax
```py
imgui.text_colored(color, text)
```

## Parameters
- **color** – (ImVec4Like) vector of 4 values ​​representing the red, green, blue, and alpha channels. Must be in the range [0.0 - 1.0].
- **text** – (str) Text to display. Must be in string format.

## Return
- None

## Usage example
```py
import imgui

def gui():
    # Red text
    imgui.text_colored(imgui.ImVec4(1.0, 0.0, 0.0, 1.0), "Hello, world!")

    # Yellow text
    imgui.text_colored(imgui.ImVec4(1.0, 1.0, 0.0, 1.0), "Goodbye, world!")

    # Dark gray text
    imgui.text_colored(imgui.ImVec4(0.2, 0.2, 0.2, 1.0), "Adios, mundo!")
```

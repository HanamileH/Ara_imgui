# Color edit widgets

`imgui.color_edit3` edits an RGB color, while `imgui.color_edit4` also edits
the alpha channel. They are convenient when the exact numeric channels should
remain visible.

## Description

The color can be passed as a list of floats or as `imgui.ImVec4`. Components are
in the `0.0`–`1.0` range. The value argument is optional; omit it or pass
`None` to reuse the previous color.

`color_edit3` returns three components, `color_edit4` returns four. The default
color is black; `color_edit4` defaults to `[0.0, 0.0, 0.0, 1.0]`.

## Syntax

```py
color = imgui.color_edit3(label, col=None, flags=0)
color = imgui.color_edit4(label, col=None, flags=0)
```

## Variants

| Function | Returns | Description |
|----------|---------|-------------|
| `imgui.color_edit3` | `list[float] / ImVec4` | RGB color. |
| `imgui.color_edit4` | `list[float] / ImVec4` | RGBA color. |

## Parameters

- **label** – (str) Visible label. Supports `##` IDs and the `++` counter.
- **col** – (ImVec4Like, optional) Current color. Omit it or pass `None` to reuse the previous value.
- **flags** – (int) Optional `ColorEditFlags`.
- **default** – (list[float] / ImVec4) Keyword-only color for the first frame.

## Return

- **color** – (list[float] / ImVec4) The new RGB or RGBA color.

## Usage example

```python
from ara_imgui import App, imgui

app = App("Color edit")

def gui():
    color = imgui.color_edit3("Color", default=[1.0, 0.5, 0.0])
    rgba = imgui.color_edit4("Overlay", default=[1.0, 1.0, 1.0, 0.5])

    imgui.text(f"RGB: {color[0]:.2f}, {color[1]:.2f}, {color[2]:.2f}")
    imgui.text(f"Alpha: {rgba[3]:.2f}")

app.run(gui)
```

## See also

- [Color picker](color_picker.md)
- [Color button](color_button.md)

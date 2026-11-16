# Color picker widgets

`imgui.color_picker3` opens a picker for RGB colors, while
`imgui.color_picker4` also edits the alpha channel. Pickers are usually shown
in a popup and are more visual than color edit widgets.

## Description

The color can be a list of floats or `imgui.ImVec4`, with components in the
`0.0`–`1.0` range. The value argument is optional; omit it or pass `None` to
reuse the previous color.

`color_picker4` also accepts `ref_col`, an optional reference color used by
some picker modes.

## Syntax

```py
color = imgui.color_picker3(label, col=None, flags=0)
color = imgui.color_picker4(label, col=None, flags=0, ref_col=None)
```

## Variants

| Function | Returns | Description |
|----------|---------|-------------|
| `imgui.color_picker3` | `list[float] / ImVec4` | RGB color picker. |
| `imgui.color_picker4` | `list[float] / ImVec4` | RGBA color picker. |

## Parameters

- **label** – (str) Visible label. Supports `##` IDs and the `++` counter.
- **col** – (ImVec4Like, optional) Current color. Omit it or pass `None` to reuse the previous value.
- **flags** – (int) Optional `ColorEditFlags`.
- **ref_col** – (ImVec4Like, optional) Reference color for `color_picker4`.
- **default** – (list[float] / ImVec4) Keyword-only color for the first frame.

## Return

- **color** – (list[float] / ImVec4) The new RGB or RGBA color.

## Usage example

```python
from ara_imgui import App, imgui

app = App("Color picker")

def gui():
    color = imgui.color_edit3("Color", default=[1.0, 0.5, 0.0])

    if imgui.button("Pick color"):
        imgui.open_popup("picker")

    if imgui.begin_popup("picker"):
        color = imgui.color_picker3("##picker", color)
        imgui.end_popup()

    imgui.color_button("##swatch", imgui.ImVec4(*color, 1.0))

app.run(gui)
```

## See also

- [Color edit](color_edit.md)
- [Color button](color_button.md)

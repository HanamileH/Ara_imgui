# Buttons

Buttons perform an action when clicked. All of them return `True` for exactly
one frame when they are pressed, so the usual pattern is an `if` around the
button call.

## Description

Ara_imgui wraps four button functions:

- `imgui.button()` draws a normal button with a visible label.
- `imgui.small_button()` draws a compact button.
- `imgui.invisible_button()` draws an invisible hit area; it is useful for
  custom widgets and drag areas.
- `imgui.arrow_button()` draws a button with one of four direction arrows.

All of them take a label (or string ID) that follows the normal `##` ID rules
and supports a trailing `++` counter. See
[Labels and IDs](../concepts.md#labels-and-ids).

## Syntax

```py
pressed = imgui.button(label, size=None)
pressed = imgui.small_button(label)
pressed = imgui.invisible_button(str_id, size, flags=0)
pressed = imgui.arrow_button(str_id, dir)
```

## Variants

| Function | Returns | Description |
|----------|---------|-------------|
| `imgui.button` | `bool` | Normal button with a visible label. |
| `imgui.small_button` | `bool` | Compact button. |
| `imgui.invisible_button` | `bool` | Invisible hit area of the requested size. |
| `imgui.arrow_button` | `bool` | Button with a direction arrow. |

## Parameters

- **label** – (str) Visible text. Use `"Text##id"` to keep the ID separate from the visible text.
- **size** – (ImVec2Like) Button size. Use `imgui.ImVec2(width, height)`; omit it to use the default size.
- **str_id** – (str) ID used for an invisible or arrow button.
- **flags** – (int) Optional button flags. See [Flags](../concepts.md#flags).
- **dir** – (Dir) Arrow direction, for example `imgui.Dir_.left` or `imgui.Dir_.right`.

## Return

- **pressed** – (bool) `True` on the frame the button was pressed.

## Usage example

```python
from ara_imgui import App, imgui

app = App("Buttons")

def gui():
    if imgui.button("Click me!"):
        print("Clicked!")

    if imgui.button("Wide button", imgui.ImVec2(200, 40)):
        print("Wide button clicked!")

    if imgui.small_button("Small"):
        print("Small button clicked!")

    if imgui.arrow_button("##right", imgui.Dir_.right):
        print("Right arrow clicked!")

app.run(gui)
```

### Unique IDs in loops

Every button in the same window needs a unique ID. When buttons are created in
a loop, use an explicit ID or the `++` counter:

```python
for row in rows:
    if imgui.button(f"Delete##row_{row.id}"):
        delete(row)
```

The `++` counter is shorter, but it depends on submission order:

```python
for row in rows:
    if imgui.button("Delete++"):
        delete(row)
```

Use `++` only when the order of rows is stable. See
[Labels and IDs](../concepts.md#labels-and-ids) for the escape sequence and
warnings.

## See also

- [Labels and IDs](../concepts.md#labels-and-ids)
- [imgui.radio_button](radio_button.md)
- [imgui.checkbox](checkbox.md)

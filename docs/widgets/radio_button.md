# imgui.radio_button

## Description

Draws a radio button. Radio buttons are used in groups: exactly one option in
the group is selected at a time.

There are two forms. The boolean form draws one radio button and returns
`True` when it was clicked; you update your own selected index. The integer
form takes the current selected index and the index represented by this
button, and returns the new selected index.

Both forms take a label that follows the normal `##` ID rules and supports a
trailing `++` counter.

## Syntax

```py
pressed = imgui.radio_button(label, active)
selected = imgui.radio_button(label, v, v_button)
```

## Variants

| Function | Returns | Description |
|----------|---------|-------------|
| `imgui.radio_button(label, active)` | `bool` | Boolean form: `True` when this radio button was clicked. |
| `imgui.radio_button(label, v, v_button)` | `tuple[bool, int]` | Integer form: returns `(clicked, new_value)`. |

## Parameters

- **label** – (str) Visible text next to the radio button.
- **active** – (bool) Whether this radio button is selected in the boolean form.
- **v** – (int) Currently selected index in the integer form.
- **v_button** – (int) Index represented by this radio button in the integer form.

## Return

- **pressed** – (bool) Boolean form: `True` on the frame the button was clicked.
- **selected** – (int) Integer form: the selected index after the click.

## Usage example

```python
from ara_imgui import App, imgui

app = App("Radio buttons")

selected = 0

def gui():
    global selected

    for index, name in enumerate(["Low", "Medium", "High"]):
        clicked, selected = imgui.radio_button(f"{name}##quality", selected, index)
        if clicked:
            print(f"Selected {name}")

    imgui.text(f"Quality: {selected}")

app.run(gui)
```

When the same visible label is used in a loop, give each radio button a unique
ID, for example `f"{name}##quality"` or use the `++` counter. See
[Labels and IDs](../concepts.md#labels-and-ids).

## See also

- [Buttons](button.md)
- [imgui.checkbox](checkbox.md)

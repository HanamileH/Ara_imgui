# Checkbox widgets

Checkboxes toggle a boolean state. `checkbox` works with a single `bool`, while
`checkbox_flags` packs several independent booleans into one integer bit mask.

## Description

`imgui.checkbox()` draws a checkbox for one `True`/`False` value. It returns the
new state.

`imgui.checkbox_flags()` draws a checkbox that represents one bit of a bit mask.
It returns the updated mask. Use it when several independent options share one
integer value (for example, a set of feature flags).

Both value arguments are optional: omit the value or pass `None` to reuse the
value from the previous frame. See [Value memory](../concepts.md#value-memory).

## Syntax

```py
checked = imgui.checkbox(label, checked=None)
flags = imgui.checkbox_flags(label, flags=None, flags_value=FLAG)
```

## Variants

| Function | Returns | Description |
|----------|---------|-------------|
| `imgui.checkbox` | `bool` | One boolean value. |
| `imgui.checkbox_flags` | `int` | One bit inside an integer bit mask. |

## Parameters

- **label** – (str) Visible text next to the checkbox.
- **checked** – (bool, optional) Current state. Omit it or pass `None` to reuse the previous value.
- **flags** – (int, optional) Current bit mask. Omit it or pass `None` to reuse the previous value.
- **flags_value** – (int) The bit that this checkbox represents.
- **default** – (bool / int) Keyword-only value for the first frame: `default=False` or `default=0`.

## Return

- **checked** – (bool) `checkbox`: the new boolean state.
- **flags** – (int) `checkbox_flags`: the updated bit mask.

## Usage example

```python
from ara_imgui import App, imgui

OPTION_A = 1 << 0
OPTION_B = 1 << 1
OPTION_C = 1 << 2

flags = 0

app = App("Checkboxes")

def gui():
    global flags

    enabled = imgui.checkbox("Enabled", default=True)
    imgui.text(f"Enabled: {enabled}")

    flags = imgui.checkbox_flags("Option A", flags, OPTION_A)
    flags = imgui.checkbox_flags("Option B", flags, OPTION_B)
    flags = imgui.checkbox_flags("Option C", flags, OPTION_C)
    imgui.text(f"Flags: {flags:#05b}")

app.run(gui)
```

`checkbox_flags` combines the current mask with the bit being toggled and
returns the new mask. When several checkboxes share one mask, keep the mask in a
variable (a global or an object attribute) and pass it to every call, as in the
example above.

A single `checkbox_flags` can also use value memory: omit `flags` and pass
`flags_value` by keyword, and it will remember its own mask between frames.

## See also

- [Value memory](../concepts.md#value-memory)
- [Buttons](button.md)

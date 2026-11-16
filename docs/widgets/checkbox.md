# imgui.checkbox

## Description

Displays a checkbox and returns its current state. The checkbox value is
returned directly; use `imgui.is_item_changed()` to detect edits.

The value argument is optional. When it is omitted or `None`, the widget reuses
the value it returned on the previous frame.

## Syntax

```py
checked = imgui.checkbox(label, checked=None)
```

## Parameters

- **label** – (str) Text displayed next to the checkbox. Supports `##` IDs and
  the `++` counter.
- **checked** – (bool, optional) Current state. Omit it or pass `None` to reuse
  the previous value.
- **default** – (bool, keyword-only) State for the first frame.

## Return

- **checked** – (bool) The current state of the checkbox.

## Usage example

```py
from ara_imgui import App, imgui

def gui():
    notifications = imgui.checkbox("Enable notifications", default=True)
    imgui.text(f"Notifications: {notifications}")

    if imgui.button("Disable"):
        imgui.set_item_value("Enable notifications", False)

app = App()
app.run(gui)
```

For a checkbox backed by a bit mask, see
[`imgui.checkbox_flags`](value_widgets.md#boolean-inputs).

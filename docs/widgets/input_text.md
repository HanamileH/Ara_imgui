# imgui.input_text

## Description

Draws a single-line text field. The function returns the current text on every
frame: the value you passed in on the first frame, the edited text after the
user types, and so on.

The value argument is optional. If you omit it or pass `None`, the widget reuses
the text it returned on the previous frame, so it keeps its own state without a
global variable. See [Value memory](../concepts.md#value-memory).

`input_text` is a **value widget**: it returns the text directly, not a
`(changed, value)` tuple. Use
[imgui.is_item_changed](is_item_changed.md) to detect edits.

## Syntax

```py
text = imgui.input_text(label, text=None, flags=0, callback=None, user_data=None)
```

## Parameters

- **label** – (str) Visible text next to the field. Use `"Name##id"` to keep a stable ID.
- **text** – (str, optional) Current text. Omit it or pass `None` to reuse the previous value.
- **flags** – (int) Optional `InputTextFlags` bit mask.
- **callback** – (callable, optional) Advanced ImGui input callback, usually `None`.
- **user_data** – (Any, optional) Data passed to `callback`.
- **default** – (str) Keyword-only text for the first frame, before anything is remembered.

## Return

- **text** – (str) The text after this frame's editing.

## Usage example

```python
from ara_imgui import App, imgui

app = App("Text input")

def gui():
    name = imgui.input_text("Name", default="")

    if imgui.is_item_changed():
        print(f"Name changed to {name!r}")

    imgui.text(f"Hello, {name or 'unknown'}!")

    if imgui.button("Clear"):
        imgui.set_item_value("Name", "")

app.run(gui)
```

### Useful flags

Flags are optional integer bit masks from `ara_imgui.flags`. For example, a
password field can be created with:

```python
from ara_imgui import flags

password = imgui.input_text(
    "Password",
    flags=flags.input_text.password,
)
```

See [Flags](../concepts.md#flags) for how bit masks work.

## See also

- [Value memory](../concepts.md#value-memory)
- [imgui.input_text_multiline](input_text_multiline.md)
- [imgui.input_text_with_hint](input_text_with_hint.md)

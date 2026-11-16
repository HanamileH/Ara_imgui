# imgui.input_text

## Description

Displays a single-line text input field. The updated string is returned
directly; use `imgui.is_item_changed()` to detect edits.

The value argument is optional. When it is omitted or `None`, the widget reuses
the value it returned on the previous frame. See
[State and IDs](state_and_ids.md#value-memory).

## Syntax

```py
text = imgui.input_text(label, text=None, flags=0, callback=None, user_data=None)
```

## Parameters

- **label** – (str) Text displayed next to the input field. Supports `##` IDs
  and the `++` counter.
- **text** – (str, optional) Current text. Omit it or pass `None` to reuse the
  previous value.
- **flags** – (int, optional) `InputTextFlags` value. See the
  [flag enums](../index.md#flag-enums).
- **callback** – (callable, optional) ImGui input-text callback.
- **user_data** – (any, optional) Data passed to the callback.
- **default** – (str, keyword-only) Value for the first frame, when no value is
  remembered yet.

## Return

- **text** – (str) The updated text value.

## Usage example

```python
from ara_imgui import App, imgui

def gui():
    name = imgui.input_text("Your name", default="")
    imgui.text(f"Hello, {name or 'unknown'}!")

app = App()
app.run(gui)
```

Remembering the value also lets you reset it from a button:

```python
if imgui.button("Clear name"):
    imgui.set_item_value("Your name", "")
```

# imgui.input_text_multiline

## Description

Displays a multi-line text input field. The updated string is returned
directly; use `imgui.is_item_changed()` to detect edits.

The value argument is optional. When it is omitted or `None`, the widget reuses
the value it returned on the previous frame. See
[State and IDs](state_and_ids.md#value-memory).

## Syntax

```py
text = imgui.input_text_multiline(label, text=None, size=None, flags=0, callback=None, user_data=None)
```

## Parameters

- **label** – (str) Text displayed next to the input field. Supports `##` IDs
  and the `++` counter.
- **text** – (str, optional) Current text. Omit it or pass `None` to reuse the
  previous value.
- **size** – (ImVec2, optional) Size of the input area. Defaults to the ImGui
  default size.
- **flags** – (int, optional) `InputTextFlags` value.
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
    description = imgui.input_text_multiline(
        "Description",
        default="",
        size=imgui.ImVec2(320, 100),
    )
    imgui.text(f"{len(description)} characters")

app = App()
app.run(gui)
```

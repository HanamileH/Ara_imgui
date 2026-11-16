# imgui.input_text_with_hint

## Description

Draws a single-line text field and displays a hint inside it while the field is
empty. The hint is not part of the value: as soon as the user types, the hint
disappears.

The value argument is the **third** argument; the hint comes first. As with the
other text inputs, the value is optional and can be reused between frames.

## Syntax

```py
text = imgui.input_text_with_hint(label, hint, text=None, flags=0, callback=None, user_data=None)
```

## Parameters

- **label** – (str) Visible text next to the field.
- **hint** – (str) Placeholder text shown while the field is empty.
- **text** – (str, optional) Current text. Omit it or pass `None` to reuse the previous value.
- **flags** – (int) Optional `InputTextFlags` bit mask.
- **callback** – (callable, optional) Advanced ImGui input callback.
- **user_data** – (Any, optional) Data passed to `callback`.
- **default** – (str) Keyword-only text for the first frame.

## Return

- **text** – (str) The text after this frame's editing.

## Usage example

```python
from ara_imgui import App, imgui

app = App("Input with hint")

def gui():
    search = imgui.input_text_with_hint("Search", "type to filter...")
    imgui.text(f"Query: {search!r}")

app.run(gui)
```

## See also

- [imgui.input_text](input_text.md)

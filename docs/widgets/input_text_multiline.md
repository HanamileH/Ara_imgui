# imgui.input_text_multiline

## Description

Draws a text field that can contain several lines. Apart from the optional
`size` parameter, it behaves like [imgui.input_text](input_text.md).

The value argument is optional. Omit it or pass `None` to reuse the text from
the previous frame.

## Syntax

```py
text = imgui.input_text_multiline(label, text=None, size=None, flags=0, callback=None, user_data=None)
```

## Parameters

- **label** – (str) Visible text next to the field.
- **text** – (str, optional) Current text. Omit it or pass `None` to reuse the previous value.
- **size** – (ImVec2Like, optional) Visible size of the text area.
- **flags** – (int) Optional `InputTextFlags` bit mask.
- **callback** – (callable, optional) Advanced ImGui input callback.
- **user_data** – (Any, optional) Data passed to `callback`.
- **default** – (str) Keyword-only text for the first frame.

## Return

- **text** – (str) The text after this frame's editing.

## Usage example

```python
from ara_imgui import App, imgui

app = App("Multiline input")

def gui():
    description = imgui.input_text_multiline(
        "Description",
        default="",
        size=imgui.ImVec2(360, 120),
    )
    imgui.text(f"{len(description)} characters")

app.run(gui)
```

## See also

- [imgui.input_text](input_text.md)
- [Value memory](../concepts.md#value-memory)

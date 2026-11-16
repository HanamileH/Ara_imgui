# imgui.button

## Description

Displays a button and returns `True` when it is pressed.

## Syntax

```py
pressed = imgui.button(label, size=None)
```

## Parameters

- **label** – (str) Text displayed on the button. Supports `##` IDs and the
  `++` counter.
- **size** – (ImVec2, optional) Button size. Defaults to the size calculated
  from the label and style.

## Return

- **pressed** – (bool) `True` if the button was pressed, otherwise `False`.

## Usage example

```py
from ara_imgui import App, imgui

def gui():
    if imgui.button("Click me!"):
        print("Button clicked!")

    if imgui.button("Custom size button", imgui.ImVec2(200, 50)):
        print("Second button clicked!")

app = App()
app.run(gui)
```

## IDs and the `++` counter

When buttons are created in a loop, give each one a unique ID. A trailing `++`
does that automatically, but only while the order is stable:

```py
for row in rows:
    if imgui.button("Delete++"):
        delete(row)
```

Prefer a stable explicit ID when rows can be reordered:

```py
for row in rows:
    if imgui.button(f"Delete##row_{row.id}"):
        delete(row)
```

See [State and IDs](state_and_ids.md#automatic-widget-ids-with).

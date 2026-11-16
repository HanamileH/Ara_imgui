# imgui.table

## Description

Context manager around the legacy `imgui.columns()` API. It sets the columns
up, optionally draws a header row, and closes the columns when the `with` block
ends. Use `imgui.next_column()` to move between cells; the legacy API
automatically wraps to the next row after the last column.

## Syntax

```py
with imgui.table(label, columns=None, headers=None, borders=True):
    ...
```

## Parameters

- **label** – (str) Table/columns label. It also follows the normal `##` ID
  rules and supports a trailing `++` counter.
- **columns** – (int, optional) Number of columns. If omitted, it is inferred
  from `headers`.
- **headers** – (list[str], optional) Header labels. When given, they are drawn
  as the first row.
- **borders** – (bool, optional) Whether to draw vertical column borders.
  Default is `True`.

At least one of `columns` and `headers` must be provided. `columns` must be
greater than zero, and `headers` cannot contain more entries than `columns`.

## Return

The context manager itself. It does not return a row value.

## Usage example

```py
from ara_imgui import App, imgui

people = [("John", 25, "Male"), ("Jane", 30, "Female")]

def gui():
    with imgui.table("People", 3, ["Name", "Age", "Sex"]):
        for name, age, sex in people:
            imgui.text(name)
            imgui.next_column()

            imgui.text(str(age))
            imgui.next_column()

            imgui.text(sex)
            imgui.next_column()

app = App()
app.run(gui)
```

`columns` can be omitted when headers are given:

```py
with imgui.table("People", headers=["Name", "Age"]):
    ...
```

For the modern table API with sorting and resizing, use `imgui.begin_table()` /
`imgui.end_table()` directly; see [Label widgets](label_widgets.md#menus-popups-tabs-and-containers).

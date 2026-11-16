# Tables

Ara_imgui offers a small context manager, `imgui.table`, for the legacy
`columns()` API. For sorting, resizing, and scrolling, use the modern
`imgui.begin_table()` API.

## Description

### Simple tables with `imgui.table`

`imgui.table()` is a context manager around `imgui.columns()`. It sets up the
columns, optionally draws a header row, and closes the columns when the block
ends. Move between cells with `imgui.next_column()`; the legacy API wraps to the
next row automatically after the last column.

At least one of `columns` and `headers` must be given. `borders` is enabled by
default.

### Modern tables with `imgui.begin_table`

For features such as sorting, resizing, scrolling, and frozen rows, use the
standard ImGui table API: `begin_table`, `table_setup_column`,
`table_headers_row`, `table_next_row`, `table_next_column`, and `end_table`.

## Syntax

```py
# Simple columns
with imgui.table(label, columns=None, headers=None, borders=True):
    ...

# Modern table
if imgui.begin_table(str_id, columns, flags=0, outer_size=None, inner_width=0.0):
    imgui.table_setup_column(label, flags=0, init_width_or_weight=0.0, user_data=0)
    imgui.table_headers_row()
    imgui.table_next_row()
    imgui.table_next_column()
    ...
    imgui.end_table()
```

## Parameters

- **label** – (str) Label of the simple table. Supports `##` IDs and `++`.
- **columns** – (int, optional) Number of columns. Inferred from `headers` when omitted.
- **headers** – (list[str], optional) Header labels drawn as the first row.
- **borders** – (bool) Whether to draw vertical borders. Default is `True`.
- **str_id** – (str) ID of a modern table.
- **flags** – (int) Optional `TableFlags` for a modern table.
- **outer_size** – (ImVec2Like, optional) Outer size of a modern table.
- **inner_width** – (float) Inner width of a modern table. Default is `0.0`.

## Return

- `imgui.table` returns only its context manager; `begin_table` returns whether the table is visible.

## Usage example

```python
from ara_imgui import App, imgui

people = [("John", 25, "Male"), ("Jane", 30, "Female")]

app = App("Tables")

def gui():
    with imgui.table("People", 3, ["Name", "Age", "Sex"]):
        for name, age, sex in people:
            imgui.text(name)
            imgui.next_column()

            imgui.text(str(age))
            imgui.next_column()

            imgui.text(sex)
            imgui.next_column()

app.run(gui)
```

### Modern table example

```python
def gui():
    if imgui.begin_table("people", 3):
        imgui.table_setup_column("Name")
        imgui.table_setup_column("Age")
        imgui.table_setup_column("Sex")
        imgui.table_headers_row()

        for name, age, sex in people:
            imgui.table_next_row()
            imgui.table_next_column()
            imgui.text(name)
            imgui.table_next_column()
            imgui.text(str(age))
            imgui.table_next_column()
            imgui.text(sex)

        imgui.end_table()
```

## See also

- [Child window](child.md)
- [Labels and IDs](../concepts.md#labels-and-ids)

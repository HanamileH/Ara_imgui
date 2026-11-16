# Label widgets

These widgets take a label or string ID and are wrapped by Ara_imgui so that a
trailing `++` produces a per-label, per-frame ID:

```python
for row in rows:
    if imgui.button("Delete++"):
        ...
```

Their return values are **not** changed: buttons return `bool`, `begin_*`
functions return whatever `imgui_bundle` returns, and so on. Only the label
argument is expanded.

See [State and IDs](state_and_ids.md#automatic-widget-ids-with) for the
counter rules, the `\++` escape, warnings, and why stable order matters.

## Buttons

| Widget | Signature | Returns |
|--------|-----------|---------|
| `imgui.button` | `button(label, size=None)` | `bool` |
| `imgui.small_button` | `small_button(label)` | `bool` |
| `imgui.invisible_button` | `invisible_button(str_id, size, flags=0)` | `bool` |
| `imgui.arrow_button` | `arrow_button(str_id, dir)` | `bool` |
| `imgui.radio_button` | `radio_button(label, active)` | `bool` |
| `imgui.radio_button` | `radio_button(label, v, v_button)` | `tuple[bool, int]` |

```python
if imgui.button("Save"):
    save()
if imgui.small_button("Cancel"):
    cancel()
```

## Selection

| Widget | Signature | Returns |
|--------|-----------|---------|
| `imgui.selectable` | `selectable(label, selected, flags=0, size=None)` | `tuple[bool, bool]` |
| `imgui.menu_item` | `menu_item(label, shortcut, selected, enabled=True)` | `tuple[bool, bool]` |
| `imgui.color_button` | `color_button(desc_id, col, flags=0, size=None)` | `bool` |

```python
clicked, selected = imgui.selectable("Row", selected)
opened, selected = imgui.menu_item("Show details", None, selected)
imgui.color_button("##swatch", color)
```

## Trees and collapsing headers

| Widget | Signature | Returns |
|--------|-----------|---------|
| `imgui.tree_node` | `tree_node(label)` | `bool` |
| `imgui.tree_node` | `tree_node(str_id, fmt)` | `bool` |
| `imgui.tree_push` | `tree_push(str_id)` | `None` |
| `imgui.collapsing_header` | `collapsing_header(label, flags=0)` | `bool` |

For a context-manager version with automatic `tree_pop()`, use
[`imgui.tree()`](tree.md).

```python
if imgui.tree_node("Advanced"):
    imgui.text("Advanced options")
    imgui.tree_pop()
```

## Menus, popups, tabs, and containers

| Widget | Signature | Returns |
|--------|-----------|---------|
| `imgui.begin` | `begin(name, p_open=None, flags=0)` | `tuple[bool, bool | None]` |
| `imgui.begin_child` | `begin_child(str_id, size=None, child_flags=0, window_flags=0)` | `bool` |
| `imgui.begin_combo` | `begin_combo(label, preview_value, flags=0)` | `bool` |
| `imgui.begin_list_box` | `begin_list_box(label, size=None)` | `bool` |
| `imgui.begin_menu` | `begin_menu(label, enabled=True)` | `bool` |
| `imgui.begin_popup` | `begin_popup(str_id, flags=0)` | `bool` |
| `imgui.begin_popup_modal` | `begin_popup_modal(name, p_open=None, flags=0)` | `tuple[bool, bool | None]` |
| `imgui.begin_tab_bar` | `begin_tab_bar(str_id, flags=0)` | `bool` |
| `imgui.begin_tab_item` | `begin_tab_item(label, p_open=None, flags=0)` | `tuple[bool, bool | None]` |
| `imgui.begin_table` | `begin_table(str_id, columns, flags=0, outer_size=None, inner_width=0.0)` | `bool` |
| `imgui.open_popup` | `open_popup(str_id, popup_flags=0)` | `bool` |

Every `begin_*` has a matching `end_*` call. For children, tables, and trees,
prefer the context managers:

```python
with imgui.child("Log"):
    imgui.text("Child content")

with imgui.table("People", 3, ["Name", "Age", "Sex"]):
    ...

with imgui.tree("Settings") as open_:
    if open_:
        imgui.text("Advanced options")
```

## Table columns

| Widget | Signature | Returns |
|--------|-----------|---------|
| `imgui.table_setup_column` | `table_setup_column(label, flags=0, init_width_or_weight=0.0, user_data=0)` | `None` |

Used inside the modern `begin_table()` API:

```python
if imgui.begin_table("people", 3):
    imgui.table_setup_column("Name")
    imgui.table_setup_column("Age")
    imgui.table_setup_column("Sex")
    imgui.table_headers_row()
    # ...
    imgui.end_table()
```

## `++` and explicit IDs

`++` is a convenience for loops whose order never changes. When the order can
change, use a stable explicit ID instead:

```python
for row in rows:
    imgui.button(f"Delete##row_{row.id}")
```

See [State and IDs](state_and_ids.md#automatic-widget-ids-with) for the full
explanation and warnings.

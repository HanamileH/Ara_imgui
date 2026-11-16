# Widget reference

Ara_imgui does not reimplement Dear ImGui. It re-exports `imgui_bundle.imgui`
and customizes a small, explicit set of widgets. The reference is split into
three groups:

| Group | What Ara_imgui changes | Reference |
|-------|------------------------|-----------|
| **Value widgets** | Return the new value directly (without the `changed` flag), remember the last value, and accept omitted/`None` values | [Value widgets](value_widgets.md) |
| **Label widgets** | Expand a trailing `++` into a per-label, per-frame ID counter | [Label widgets](label_widgets.md) |
| **Everything else** | Passed through unchanged from `imgui_bundle.imgui` | [imgui_bundle](https://github.com/pthom/imgui_bundle) |

## Common concepts

- **Value widgets** return the new value, not `(changed, value)`. Use
  [`imgui.is_item_changed()`](state_and_ids.md#is_item_changed) right after the
  widget to detect edits.
- **Labels and IDs**: Dear ImGui hashes the part of a label after `##`. Use
  `"Visible label##stable_id"` when the visible text is not unique.
- **Remembered values**: omit the value argument or pass `None` to reuse the
  value returned on the previous frame. `default=` sets the value for the first
  frame. See [State and IDs](state_and_ids.md#value-memory).
- **`++` counters**: a label ending in `++` becomes unique per submission and
  frame. This is convenient for loops but depends on submission order, so it is
  not a replacement for a stable explicit ID. See
  [State and IDs](state_and_ids.md#automatic-widget-ids-with).

## Text and layout helpers

These widgets are not wrapped: they behave exactly like their `imgui_bundle`
counterparts, and use the standard Dear ImGui label/ID rules.

| Function | Description |
|----------|-------------|
| [imgui.text](text.md) | Plain text |
| [imgui.text_colored](text_colored.md) | Colored text |
| [imgui.text_disabled](text_disabled.md) | Dimmed text |
| [imgui.text_wrapped](text_wrapped.md) | Word-wrapped text |
| [imgui.text_link](text_link.md) | Clickable text link |
| [imgui.text_link_open_url](text_link_open_url.md) | Text link that opens a URL |
| [imgui.separator](separator.md) | Horizontal separator |

## Context managers

| Context manager | Wraps |
|-----------------|-------|
| [imgui.child](child.md) | `begin_child()` / `end_child()` |
| [imgui.table](table.md) | `columns()` / `columns(1)` |
| [imgui.tree](tree.md) | `tree_node()` / `tree_pop()` |

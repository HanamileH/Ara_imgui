# Widget overview

Ara_imgui wraps a focused set of Dear ImGui widgets and passes the rest
through unchanged. Use this page as a map of the widget documentation.

If you are new to the library, read [Core concepts](../concepts.md) first.

## Text

| Widget | Description |
|--------|-------------|
| [Text](text.md) | Draws plain, non-interactive text. |
| [Text colored](text_colored.md) | Draws text with an explicit color. |
| [Text disabled](text_disabled.md) | Draws dimmed text for unavailable options. |
| [Text wrapped](text_wrapped.md) | Draws text that wraps at the edge of the window. |
| [Text link](text_link.md) | Draws clickable text that looks like a link. |
| [Text link open url](text_link_open_url.md) | Draws a link that opens a URL when clicked. |
| [Separator](separator.md) | Draws a horizontal separator line. |

## Buttons and selection

| Widget | Description |
|--------|-------------|
| [Buttons](button.md) | Clickable controls: `button`, `small_button`, `invisible_button`, and `arrow_button`. |
| [Radio button](radio_button.md) | A radio button for choosing one option from a group. |
| [Checkbox](checkbox.md) | Toggle booleans: `checkbox` and `checkbox_flags`. |
| [Selectable](selectable.md) | A clickable row that can report selection. |
| [Menus](menus.md) | Menu entries and submenus: `menu_item` and `begin_menu`. |
| [Color button](color_button.md) | A clickable color swatch. |

## Inputs

| Widget | Description |
|--------|-------------|
| [Input text](input_text.md) | A single-line text input. |
| [Input text multiline](input_text_multiline.md) | A multi-line text input. |
| [Input text with hint](input_text_with_hint.md) | A text input that shows a hint while empty. |
| [Integer inputs](input_int.md) | Scalar and multi-component integer input fields. |
| [Float inputs](input_float.md) | Scalar, multi-component, and double-precision numeric inputs. |
| [Drag integers](drag_int.md) | Drag integer fields, including a two-handle range. |
| [Drag floats](drag_float.md) | Drag float fields, including a two-handle range. |
| [Integer sliders](slider_int.md) | Horizontal and vertical integer sliders. |
| [Float sliders](slider_float.md) | Horizontal and vertical float sliders, plus an angle slider. |
| [Combo box](combo.md) | Choose one item from a dropdown list. |
| [List box](list_box.md) | A scrollable list of options. |
| [Color edit](color_edit.md) | RGB and RGBA color editing widgets. |
| [Color picker](color_picker.md) | RGB and RGBA color pickers. |

## Trees and containers

| Widget | Description |
|--------|-------------|
| [Trees](tree.md) | Expandable sections: `tree_node`, `tree_push`, `collapsing_header`, and the `tree` context manager. |
| [Child window](child.md) | A scrollable child region inside the current window. |
| [Tables](table.md) | Simple column layouts with `imgui.table`, and the modern `begin_table` API. |
| [Window](window.md) | Create your own floating window inside the app. |
| [Popups](popups.md) | Context menus, modal dialogs, and custom popups. |
| [Tabs](tabs.md) | Tab bars and tab items. |

## State helpers

| Widget | Description |
|--------|-------------|
| [Value memory](value_memory.md) | How value widgets remember their previous value. |
| [Labels and IDs](labels_and_ids.md) | How visible labels, `##` IDs, and the `++` counter work. |
| [is_item_changed](is_item_changed.md) | Detect whether the last value widget changed. |
| [set_item_value](set_item_value.md) | Change the remembered value of a widget by ID. |

## See also

- [Core concepts](../concepts.md)
- [Cheat sheet](../cheat_sheet.md)

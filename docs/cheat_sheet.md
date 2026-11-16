# Widget cheat sheet

Every widget documented by Ara_imgui is listed below. Follow the links
for complete signatures, parameters, return values, and examples.

New to the library? Start with [Core concepts](concepts.md), especially
[Labels and IDs](concepts.md#labels-and-ids) and
[Value memory](concepts.md#value-memory).

## Text

| Widget | Description |
|--------|-------------|
| [Text](widgets/text.md) | Draws plain, non-interactive text. |
| [Text colored](widgets/text_colored.md) | Draws text with an explicit color. |
| [Text disabled](widgets/text_disabled.md) | Draws dimmed text for unavailable options. |
| [Text wrapped](widgets/text_wrapped.md) | Draws text that wraps at the edge of the window. |
| [Text link](widgets/text_link.md) | Draws clickable text that looks like a link. |
| [Text link open url](widgets/text_link_open_url.md) | Draws a link that opens a URL when clicked. |
| [Separator](widgets/separator.md) | Draws a horizontal separator line. |

## Buttons and selection

| Widget | Description |
|--------|-------------|
| [Buttons](widgets/button.md) | Clickable controls: `button`, `small_button`, `invisible_button`, and `arrow_button`. |
| [Radio button](widgets/radio_button.md) | A radio button for choosing one option from a group. |
| [Checkbox](widgets/checkbox.md) | Toggle booleans: `checkbox` and `checkbox_flags`. |
| [Selectable](widgets/selectable.md) | A clickable row that can report selection. |
| [Menus](widgets/menus.md) | Menu entries and submenus: `menu_item` and `begin_menu`. |
| [Color button](widgets/color_button.md) | A clickable color swatch. |

## Inputs

| Widget | Description |
|--------|-------------|
| [Input text](widgets/input_text.md) | A single-line text input. |
| [Input text multiline](widgets/input_text_multiline.md) | A multi-line text input. |
| [Input text with hint](widgets/input_text_with_hint.md) | A text input that shows a hint while empty. |
| [Integer inputs](widgets/input_int.md) | Scalar and multi-component integer input fields. |
| [Float inputs](widgets/input_float.md) | Scalar, multi-component, and double-precision numeric inputs. |
| [Drag integers](widgets/drag_int.md) | Drag integer fields, including a two-handle range. |
| [Drag floats](widgets/drag_float.md) | Drag float fields, including a two-handle range. |
| [Integer sliders](widgets/slider_int.md) | Horizontal and vertical integer sliders. |
| [Float sliders](widgets/slider_float.md) | Horizontal and vertical float sliders, plus an angle slider. |
| [Combo box](widgets/combo.md) | Choose one item from a dropdown list. |
| [List box](widgets/list_box.md) | A scrollable list of options. |
| [Color edit](widgets/color_edit.md) | RGB and RGBA color editing widgets. |
| [Color picker](widgets/color_picker.md) | RGB and RGBA color pickers. |

## Trees and containers

| Widget | Description |
|--------|-------------|
| [Trees](widgets/tree.md) | Expandable sections: `tree_node`, `tree_push`, `collapsing_header`, and the `tree` context manager. |
| [Child window](widgets/child.md) | A scrollable child region inside the current window. |
| [Tables](widgets/table.md) | Simple column layouts with `imgui.table`, and the modern `begin_table` API. |
| [Window](widgets/window.md) | Create your own floating window inside the app. |
| [Popups](widgets/popups.md) | Context menus, modal dialogs, and custom popups. |
| [Tabs](widgets/tabs.md) | Tab bars and tab items. |

## State helpers

| Widget | Description |
|--------|-------------|
| [Value memory](widgets/value_memory.md) | How value widgets remember their previous value. |
| [Labels and IDs](widgets/labels_and_ids.md) | How visible labels, `##` IDs, and the `++` counter work. |
| [is_item_changed](widgets/is_item_changed.md) | Detect whether the last value widget changed. |
| [set_item_value](widgets/set_item_value.md) | Change the remembered value of a widget by ID. |

## See also

- [Core concepts](concepts.md)
- [Widget overview](widgets/index.md)

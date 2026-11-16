# Widget cheat sheet

This page lists every widget that Ara_imgui wraps or adds. Widgets are grouped
by what they do. For full signatures, parameters, and return values, follow the
links to the reference pages.

Everything not listed here is re-exported from `imgui_bundle.imgui` unchanged.

## State helpers

| Function | Description |
|----------|-------------|
| [`imgui.is_item_changed`](widgets/state_and_ids.md#is_item_changed) | Whether the last submitted value widget changed. |
| [`imgui.set_item_value`](widgets/state_and_ids.md#set_item_value) | Change the remembered value of a widget by ID. |
| [`++` label counter](widgets/state_and_ids.md#automatic-widget-ids-with) | Generate a per-label, per-frame ID for repeated widgets. |

## Text displaying

| Widget | Description |
|--------|-------------|
| [imgui.text](widgets/text.md) | Displays a simple text label. |
| [imgui.text_colored](widgets/text_colored.md) | Displays a text label with a custom color. |
| [imgui.text_disabled](widgets/text_disabled.md) | Displays a text label with a disabled appearance. |
| [imgui.text_wrapped](widgets/text_wrapped.md) | Displays a text label with word wrapping. |
| [imgui.text_link](widgets/text_link.md) | Displays a text label with a hyperlink appearance. |
| [imgui.text_link_open_url](widgets/text_link_open_url.md) | Displays a hyperlink that opens a URL when clicked. |
| [imgui.separator](widgets/separator.md) | Draws a horizontal separator line. |

## Buttons and boolean inputs

| Widget | Description |
|--------|-------------|
| [imgui.button](widgets/button.md) | Clickable button. |
| [imgui.small_button](widgets/label_widgets.md#buttons) | Button using the small button style. |
| [imgui.invisible_button](widgets/label_widgets.md#buttons) | Invisible button useful for custom hit areas. |
| [imgui.arrow_button](widgets/label_widgets.md#buttons) | Button with a direction arrow. |
| [imgui.radio_button](widgets/radio_button.md) | Radio button for mutually exclusive choices. |
| [imgui.checkbox](widgets/checkbox.md) | Checkbox for a boolean value. |
| [imgui.checkbox_flags](widgets/value_widgets.md#boolean-inputs) | Checkbox packed into a bit mask of flags. |

## Selection

| Widget | Description |
|--------|-------------|
| [imgui.combo](widgets/combo.md) | Dropdown list of string items. |
| [`imgui.list_box`](widgets/value_widgets.md#selection) | Scrollable list box; returns the selected index. |
| [`imgui.selectable`](widgets/label_widgets.md#selection) | Selectable row; can report click and selection state. |
| [`imgui.menu_item`](widgets/label_widgets.md#selection) | Menu entry with an optional shortcut and check mark. |
| [`imgui.color_button`](widgets/label_widgets.md#selection) | Color swatch that can be clicked. |

## Text inputs

| Widget | Description |
|--------|-------------|
| [imgui.input_text](widgets/input_text.md) | Single-line text input. |
| [imgui.input_text_multiline](widgets/input_text_multiline.md) | Multi-line text input. |
| [`imgui.input_text_with_hint`](widgets/value_widgets.md#text) | Text input that shows a hint when empty. |

## Integer inputs

| Widget | Description |
|--------|-------------|
| [imgui.input_int](widgets/input_int.md) | Integer input field. |
| [`imgui.input_int2` / `input_int3` / `input_int4`](widgets/value_widgets.md#integers) | 2, 3, or 4 integer input fields. |
| [`imgui.drag_int` / `drag_int2` / `drag_int3` / `drag_int4`](widgets/value_widgets.md#integers) | Integer drag fields. |
| [`imgui.drag_int_range2`](widgets/value_widgets.md#integers) | Two-handle integer range. |
| [`imgui.slider_int` / `slider_int2` / `slider_int3` / `slider_int4`](widgets/value_widgets.md#integers) | Integer sliders. |
| [`imgui.v_slider_int`](widgets/value_widgets.md#integers) | Vertical integer slider. |

## Float inputs

| Widget | Description |
|--------|-------------|
| [imgui.input_float](widgets/input_float.md) | Float input field. |
| [`imgui.input_float2` / `input_float3` / `input_float4`](widgets/value_widgets.md#floats) | 2, 3, or 4 float input fields. |
| [`imgui.input_double`](widgets/value_widgets.md#floats) | Double-precision input field. |
| [`imgui.drag_float` / `drag_float2` / `drag_float3` / `drag_float4`](widgets/value_widgets.md#floats) | Float drag fields. |
| [`imgui.drag_float_range2`](widgets/value_widgets.md#floats) | Two-handle float range. |
| [`imgui.slider_float` / `slider_float2` / `slider_float3` / `slider_float4`](widgets/value_widgets.md#floats) | Float sliders. |
| [`imgui.slider_angle`](widgets/value_widgets.md#floats) | Angle slider. |
| [`imgui.v_slider_float`](widgets/value_widgets.md#floats) | Vertical float slider. |

## Colors

| Widget | Description |
|--------|-------------|
| [`imgui.color_edit3` / `color_edit4`](widgets/value_widgets.md#colors) | RGB / RGBA color editing widget. |
| [`imgui.color_picker3` / `color_picker4`](widgets/value_widgets.md#colors) | RGB / RGBA color picker. |

## Trees

| Widget | Description |
|--------|-------------|
| [`imgui.tree_node`](widgets/label_widgets.md#trees-and-collapsing-headers) | Expandable tree node. |
| [`imgui.tree_push`](widgets/label_widgets.md#trees-and-collapsing-headers) | Push an ID onto the tree ID stack. |
| [`imgui.collapsing_header`](widgets/label_widgets.md#trees-and-collapsing-headers) | Collapsible section header. |
| [imgui.tree](widgets/tree.md) | Context manager for `tree_node` / `tree_pop`. |

## Menus, popups, tabs, and containers

| Widget | Description |
|--------|-------------|
| [`imgui.begin`](widgets/label_widgets.md#menus-popups-tabs-and-containers) | Begin a window. |
| [imgui.child](widgets/child.md) | Context manager for a child window. |
| [`imgui.begin_combo`](widgets/label_widgets.md#menus-popups-tabs-and-containers) | Begin a custom combo popup. |
| [`imgui.begin_list_box`](widgets/label_widgets.md#menus-popups-tabs-and-containers) | Begin a list box. |
| [`imgui.begin_menu`](widgets/label_widgets.md#menus-popups-tabs-and-containers) | Begin a menu. |
| [`imgui.begin_popup`](widgets/label_widgets.md#menus-popups-tabs-and-containers) | Begin a popup. |
| [`imgui.begin_popup_modal`](widgets/label_widgets.md#menus-popups-tabs-and-containers) | Begin a modal popup. |
| [`imgui.begin_tab_bar`](widgets/label_widgets.md#menus-popups-tabs-and-containers) | Begin a tab bar. |
| [`imgui.begin_tab_item`](widgets/label_widgets.md#menus-popups-tabs-and-containers) | Begin a tab item. |
| [`imgui.begin_table`](widgets/label_widgets.md#menus-popups-tabs-and-containers) | Begin a modern table. |
| [`imgui.open_popup`](widgets/label_widgets.md#menus-popups-tabs-and-containers) | Open a popup by ID. |
| [`imgui.table_setup_column`](widgets/label_widgets.md#table-columns) | Declare a modern table column. |
| [imgui.table](widgets/table.md) | Context manager for the legacy `columns()` API. |

## See also

- [Value widgets](widgets/value_widgets.md)
- [Label widgets](widgets/label_widgets.md)
- [State and IDs](widgets/state_and_ids.md)

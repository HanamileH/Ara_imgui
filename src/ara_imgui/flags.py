from imgui_bundle import imgui as _imgui

# Windows and containers
window = _imgui.WindowFlags_
child = _imgui.ChildFlags_
popup = _imgui.PopupFlags_

# Widgets
button = _imgui.ButtonFlags_
combo = _imgui.ComboFlags_
input = _imgui.InputFlags_
input_text = _imgui.InputTextFlags_
item = _imgui.ItemFlags_
list_clipper = _imgui.ListClipperFlags_
multi_select = _imgui.MultiSelectFlags_
selectable = _imgui.SelectableFlags_
slider = _imgui.SliderFlags_
tree_node = _imgui.TreeNodeFlags_

# Tables and tabs
table = _imgui.TableFlags_
table_column = _imgui.TableColumnFlags_
table_row = _imgui.TableRowFlags_
tab_bar = _imgui.TabBarFlags_
tab_item = _imgui.TabItemFlags_

# Interaction and state
config = _imgui.ConfigFlags_
focused = _imgui.FocusedFlags_
hovered = _imgui.HoveredFlags_
drag_drop = _imgui.DragDropFlags_
color_edit = _imgui.ColorEditFlags_
dock_node = _imgui.DockNodeFlags_
viewport = _imgui.ViewportFlags_
backend = _imgui.BackendFlags_

# Drawing and fonts
draw = _imgui.ImDrawFlags_
draw_list = _imgui.ImDrawListFlags_
font = _imgui.ImFontFlags_
font_atlas = _imgui.ImFontAtlasFlags_

"""Tests for the grouped flag enums in ``ara_imgui.flags``."""

import types

from imgui_bundle import imgui as raw_imgui

from ara_imgui import flags

GROUPS = {
    "backend": "BackendFlags_",
    "button": "ButtonFlags_",
    "child": "ChildFlags_",
    "color_edit": "ColorEditFlags_",
    "combo": "ComboFlags_",
    "config": "ConfigFlags_",
    "dock_node": "DockNodeFlags_",
    "drag_drop": "DragDropFlags_",
    "draw": "ImDrawFlags_",
    "draw_list": "ImDrawListFlags_",
    "focused": "FocusedFlags_",
    "font": "ImFontFlags_",
    "font_atlas": "ImFontAtlasFlags_",
    "hovered": "HoveredFlags_",
    "input": "InputFlags_",
    "input_text": "InputTextFlags_",
    "item": "ItemFlags_",
    "list_clipper": "ListClipperFlags_",
    "multi_select": "MultiSelectFlags_",
    "popup": "PopupFlags_",
    "selectable": "SelectableFlags_",
    "slider": "SliderFlags_",
    "tab_bar": "TabBarFlags_",
    "tab_item": "TabItemFlags_",
    "table": "TableFlags_",
    "table_column": "TableColumnFlags_",
    "table_row": "TableRowFlags_",
    "tree_node": "TreeNodeFlags_",
    "viewport": "ViewportFlags_",
    "window": "WindowFlags_",
}


def test_flags_is_a_module():
    assert isinstance(flags, types.ModuleType)


def test_groups_map_to_imgui_enums():
    for group, enum_name in GROUPS.items():
        assert getattr(flags, group) is getattr(raw_imgui, enum_name)


def test_every_group_is_an_enum_class():
    for group in GROUPS:
        enum = getattr(flags, group)
        assert isinstance(enum, type)
        assert hasattr(enum, "__members__")


def test_flag_values_can_be_combined():
    combined = (
        flags.input_text.chars_uppercase
        | flags.input_text.chars_no_blank
        | flags.input_text.password
    )

    assert combined & flags.input_text.chars_uppercase
    assert combined & flags.input_text.chars_no_blank
    assert combined & flags.input_text.password

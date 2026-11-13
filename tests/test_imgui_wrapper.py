"""Tests for the value-oriented imgui proxy.

These tests do not create an ImGui context: the proxy logic is exercised with
a fake module, and the curated widget list is checked against the real
binding that is installed.
"""

import ast
import types
from pathlib import Path

import ara_imgui
from imgui_bundle import imgui as raw_imgui

from ara_imgui import imgui
from ara_imgui._imgui import (
    CHANGED_WIDGETS,
    VALUE_SPECS,
    ImguiProxy,
    unwrap_changed_result,
)


class _FakeImgui:
    """Stand-in for ``imgui_bundle.imgui`` with a few representative widgets."""

    def input_text(self, label, value):
        return True, value.upper()

    def checkbox(self, label, value):
        return False, not value

    def combo(self, label, current, items):
        return True, len(items) - 1

    def drag_float_range2(self, label, minimum, maximum):
        return True, minimum, maximum

    def button(self, label):
        return True

    def text(self, value):
        return None

    def is_item_edited(self):
        return True


class _ValueEchoImgui:
    """Fake binding that returns the value it was given, unchanged."""

    def __init__(self):
        self.calls = []

    def input_text(self, label, str, flags=0, callback=None, user_data=None):
        self.calls.append(("input_text", label, str))
        return True, str

    def input_int(self, label, v, step=1, step_fast=100, flags=0):
        self.calls.append(("input_int", label, v))
        return True, v

    def combo(self, label, current_item, items, popup_max_height_in_items=-1):
        self.calls.append(("combo", label, current_item))
        return True, current_item

    def drag_float_range2(
        self,
        label,
        v_current_min,
        v_current_max,
        v_speed=1.0,
        v_min=0.0,
        v_max=0.0,
        format="%.3",
        format_max=None,
        flags=0,
    ):
        self.calls.append(("drag_float_range2", label, v_current_min, v_current_max))
        return True, v_current_min, v_current_max


def test_changed_widgets_exist_in_installed_binding():
    missing = [name for name in CHANGED_WIDGETS if not hasattr(raw_imgui, name)]
    assert missing == []


def test_unwrap_single_value():
    assert unwrap_changed_result((True, "text")) == "text"
    assert unwrap_changed_result((False, 0)) == 0


def test_unwrap_multiple_values():
    assert unwrap_changed_result((True, 0.2, 0.8)) == (0.2, 0.8)


def test_unwrap_ignores_results_without_changed_flag():
    assert unwrap_changed_result(True) is True
    assert unwrap_changed_result(None) is None
    assert unwrap_changed_result((1, 2)) == (1, 2)


def test_proxy_returns_value_only():
    proxy = ImguiProxy(_FakeImgui())

    assert proxy.input_text("Name", "abc") == "ABC"
    assert proxy.checkbox("Flag", False) is True
    assert proxy.combo("Mode", 0, ["a", "b", "c"]) == 2
    assert proxy.drag_float_range2("Range", 0.2, 0.8) == (0.2, 0.8)


def test_proxy_passes_through_other_functions():
    proxy = ImguiProxy(_FakeImgui())

    assert proxy.button("Click") is True
    assert proxy.text("hello") is None


def test_every_changed_widget_has_a_value_spec():
    assert set(VALUE_SPECS) == set(CHANGED_WIDGETS)


def test_widget_value_can_be_omitted_and_is_remembered():
    proxy = ImguiProxy(_ValueEchoImgui())

    # First frame: no remembered value, so the per-widget default is used.
    assert proxy.input_text("Name") == ""
    assert proxy.input_text("Name", "Michail") == "Michail"
    # The next frame may omit the value again and gets the previous result.
    assert proxy.input_text("Name") == "Michail"


def test_none_value_reuses_the_remembered_value():
    proxy = ImguiProxy(_ValueEchoImgui())

    assert proxy.input_int("Age", 25) == 25
    assert proxy.input_int("Age", None) == 25
    assert proxy.input_int("Age") == 25


def test_explicit_value_overwrites_the_memory():
    proxy = ImguiProxy(_ValueEchoImgui())

    assert proxy.input_int("Age", 25) == 25
    assert proxy.input_int("Age", 40) == 40
    assert proxy.input_int("Age") == 40


def test_default_is_used_only_until_a_value_is_returned():
    proxy = ImguiProxy(_ValueEchoImgui())

    assert proxy.input_int("Age##input_id", None, default=18) == 18
    assert proxy.input_int("Age##input_id") == 18

    assert proxy.input_int("Age##input_id", 40) == 40
    # The explicit default no longer applies: memory wins.
    assert proxy.input_int("Age##input_id", None, default=18) == 40


def test_widgets_with_the_same_id_share_their_value():
    proxy = ImguiProxy(_ValueEchoImgui())

    assert proxy.input_int("Age##input_id", 30) == 30
    assert proxy.input_int("Years##input_id") == 30


def test_widgets_with_different_ids_keep_separate_values():
    proxy = ImguiProxy(_ValueEchoImgui())

    assert proxy.input_int("first", 1) == 1
    assert proxy.input_int("second", 2) == 2
    assert proxy.input_int("first") == 1
    assert proxy.input_int("second") == 2


def test_combo_value_can_be_omitted():
    proxy = ImguiProxy(_ValueEchoImgui())

    assert proxy.combo("Option", items=["One", "Two", "Three"]) == 0
    assert proxy.combo("Option", 2, ["One", "Two", "Three"]) == 2
    assert proxy.combo("Option", items=["One", "Two", "Three"]) == 2


def test_multi_value_widget_can_be_omitted():
    proxy = ImguiProxy(_ValueEchoImgui())

    assert proxy.drag_float_range2("Range") == (0.0, 0.0)
    assert proxy.drag_float_range2("Range", 0.2, 0.8) == (0.2, 0.8)
    assert proxy.drag_float_range2("Range") == (0.2, 0.8)


def test_multi_value_widget_fills_missing_half_from_memory():
    proxy = ImguiProxy(_ValueEchoImgui())

    assert proxy.drag_float_range2("Range", 0.2, 0.8) == (0.2, 0.8)
    assert proxy.drag_float_range2("Range", 0.4, None) == (0.4, 0.8)


def test_default_can_be_passed_as_keyword_for_a_multi_value_widget():
    proxy = ImguiProxy(_ValueEchoImgui())

    assert proxy.drag_float_range2("Range", default=(1.0, 2.0)) == (1.0, 2.0)


def test_set_item_value_sets_the_remembered_value():
    proxy = ImguiProxy(_ValueEchoImgui())

    proxy.set_item_value("Name", "Anna")
    assert proxy.input_text("Name") == "Anna"


def test_set_item_value_accepts_the_id_part_of_the_label():
    proxy = ImguiProxy(_ValueEchoImgui())

    proxy.set_item_value("input_id", 42)
    assert proxy.input_int("Age##input_id") == 42
    assert proxy.input_int("Years##input_id") == 42


def test_set_item_value_does_not_override_an_explicit_value():
    proxy = ImguiProxy(_ValueEchoImgui())

    proxy.set_item_value("Age", 1)
    assert proxy.input_int("Age", 5) == 5
    assert proxy.input_int("Age") == 5


def test_set_item_value_none_forgets_the_value():
    proxy = ImguiProxy(_ValueEchoImgui())

    assert proxy.input_int("Age##input_id", 25, default=18) == 25
    proxy.set_item_value("Age##input_id", None)
    assert proxy.input_int("Age##input_id", default=18) == 18


def test_set_item_value_supports_multi_value_widgets():
    proxy = ImguiProxy(_ValueEchoImgui())

    proxy.set_item_value("Range", (0.25, 0.75))
    assert proxy.drag_float_range2("Range") == (0.25, 0.75)


def test_set_item_value_rejects_a_none_id():
    proxy = ImguiProxy(_ValueEchoImgui())

    try:
        proxy.set_item_value(None, 1)
    except ValueError:
        pass
    else:
        raise AssertionError("set_item_value(None, ...) must raise ValueError")


def test_public_imgui_has_set_item_value():
    assert hasattr(imgui, "set_item_value")
    assert callable(imgui.set_item_value)


def test_proxy_exposes_raw_module():
    fake = _FakeImgui()
    proxy = ImguiProxy(fake)

    assert proxy.raw is fake


def test_is_item_changed_uses_edited_flag_fallback():
    class FakeWithEdited:
        def is_item_edited(self):
            return False

    assert ImguiProxy(FakeWithEdited()).is_item_changed() is False


def test_is_item_changed_prefers_native_implementation():
    class FakeWithNative:
        def is_item_changed(self):
            return True

        def is_item_edited(self):
            return False

    assert ImguiProxy(FakeWithNative()).is_item_changed() is True


def test_public_imgui_wraps_value_widgets_only():
    assert imgui.input_text is not raw_imgui.input_text
    assert imgui.input_text.__wrapped__ is raw_imgui.input_text
    assert imgui.combo.__wrapped__ is raw_imgui.combo

    assert imgui.button is raw_imgui.button
    assert imgui.begin is raw_imgui.begin
    assert imgui.is_item_hovered is raw_imgui.is_item_hovered
    assert imgui.ImVec2 is raw_imgui.ImVec2


def test_public_imgui_has_is_item_changed():
    assert hasattr(imgui, "is_item_changed")
    assert callable(imgui.is_item_changed)


def test_proxy_caches_wrapped_functions():
    proxy = ImguiProxy(_FakeImgui())
    assert proxy.input_text is proxy.input_text


def test_public_imgui_is_a_real_module():
    assert isinstance(imgui, types.ModuleType)
    assert imgui.__name__ == "ara_imgui.imgui"
    assert imgui.raw is raw_imgui
    assert imgui.get_io is raw_imgui.get_io


def test_type_stub_is_shipped_and_declares_the_public_api():
    package = Path(ara_imgui.__file__).parent
    assert (package / "py.typed").is_file()

    stub_path = package / "imgui.pyi"
    assert stub_path.is_file()

    stub = ast.parse(stub_path.read_text(encoding="utf-8"))
    functions = {
        node.name for node in stub.body if isinstance(node, ast.FunctionDef)
    }
    assert set(CHANGED_WIDGETS) <= functions
    assert {"child", "table", "tree", "is_item_changed", "set_item_value"} <= functions


def test_type_stub_does_not_return_changed_flags():
    stub_path = Path(ara_imgui.__file__).with_name("imgui.pyi")
    stub = ast.parse(stub_path.read_text(encoding="utf-8"))

    for node in stub.body:
        if not isinstance(node, ast.FunctionDef):
            continue
        if node.name not in CHANGED_WIDGETS:
            continue

        annotation = ast.unparse(node.returns)
        assert not annotation.startswith("Tuple[bool"), (node.name, annotation)


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
    assert {"child", "table", "tree", "is_item_changed"} <= functions


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


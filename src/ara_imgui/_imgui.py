from __future__ import annotations
import functools
from typing import Any, Callable, FrozenSet
from imgui_bundle import imgui as _raw_imgui

__all__ = [
    "CHANGED_WIDGETS",
    "ImguiProxy",
    "create_imgui_proxy",
    "unwrap_changed_result",
]


# Widgets whose binding returns ``(changed, value)`` -- or ``(changed, first,
# second)`` for range widgets.  The list is explicit on purpose: dropping the
# leading boolean from *every* tuple would also strip meaningful flags from
# ``begin`` (visible), ``begin_popup_modal`` (opened), ``collapsing_header``,
# ``menu_item``, ``selectable`` and similar functions.
#
# The tests check that each name still exists in the installed binding, so a
# future imgui_bundle release that renames or removes a widget fails loudly.
CHANGED_WIDGETS: FrozenSet[str] = frozenset(
    {
        # Boolean inputs
        "checkbox",
        "checkbox_flags",
        
        # Colors
        "color_edit3",
        "color_edit4",
        "color_picker3",
        "color_picker4",

        # Selection
        "combo",
        "list_box",

        # Text
        "input_text",
        "input_text_multiline",
        "input_text_with_hint",

        # Integers
        "input_int",
        "input_int2",
        "input_int3",
        "input_int4",
        "drag_int",
        "drag_int2",
        "drag_int3",
        "drag_int4",
        "drag_int_range2",
        "slider_int",
        "slider_int2",
        "slider_int3",
        "slider_int4",
        "v_slider_int",

        # Floats
        "input_float",
        "input_float2",
        "input_float3",
        "input_float4",
        "input_double",
        "drag_float",
        "drag_float2",
        "drag_float3",
        "drag_float4",
        "drag_float_range2",
        "slider_float",
        "slider_float2",
        "slider_float3",
        "slider_float4",
        "slider_angle",
        "v_slider_float",
    }
)


def unwrap_changed_result(result: Any) -> Any:
    """Return a widget result without its leading ``changed`` flag.

    ``(changed, value)`` becomes ``value`` and ``(changed, first, second)``
    becomes ``(first, second)``.  Anything that does not look like a
    ``(changed, ...)`` pair is returned as is, so a binding that stops adding
    the flag keeps working instead of silently corrupting the result.
    """
    if (
        isinstance(result, tuple)
        and len(result) > 1
        and isinstance(result[0], bool)
    ):
        return result[1] if len(result) == 2 else result[1:]
    return result


def _wrap_changed(func: Callable[..., Any]) -> Callable[..., Any]:
    """Build the ``changed``-less variant of a single imgui function."""

    @functools.wraps(func)
    def wrapper(*args: Any, **kwargs: Any) -> Any:
        return unwrap_changed_result(func(*args, **kwargs))

    return wrapper


class ImguiProxy:
    """Module-like proxy that wraps the value widgets of ``imgui_bundle.imgui``.

    Every attribute that is not a wrapped widget is forwarded to the
    underlying module unchanged, so ``imgui.ImVec2``, ``imgui.begin``,
    ``imgui.button`` and friends behave exactly as before.  The original
    module stays available as :attr:`raw`.
    """

    __slots__ = ("_module", "_cache")

    def __init__(self, module: Any = _raw_imgui) -> None:
        object.__setattr__(self, "_module", module)
        object.__setattr__(self, "_cache", {})

    def __getattr__(self, name: str) -> Any:
        module = object.__getattribute__(self, "_module")
        cache = object.__getattribute__(self, "_cache")

        if name in cache:
            return cache[name]

        if name == "raw":
            value = module
        else:
            attribute = getattr(module, name)
            if name in CHANGED_WIDGETS:
                value = _wrap_changed(attribute)
            else:
                value = attribute

        cache[name] = value
        return value

    def is_item_changed(self) -> bool:
        """``True`` when the last submitted widget changed its value.

        Call this immediately after the widget you are interested in: like
        ``imgui.is_item_edited()``, it refers to the last submitted item.

        ``imgui_bundle`` does not ship ``is_item_changed`` yet, so it is
        implemented on top of ``is_item_edited`` -- the very flag Dear ImGui
        sets when a widget returns ``changed == True``.
        """
        module = object.__getattribute__(self, "_module")
        checker = getattr(module, "is_item_changed", None)
        if checker is None:
            checker = module.is_item_edited
        return bool(checker())

    def __dir__(self) -> list:
        module = object.__getattribute__(self, "_module")
        return sorted(set(dir(module)) | {"is_item_changed", "raw"})

    def __repr__(self) -> str:
        module = object.__getattribute__(self, "_module")
        try:
            version = module.get_version()
        except Exception:  # pragma: no cover - depends on the binding build
            version = "unknown"
        return f"<ara_imgui.imgui proxy (Dear ImGui {version})>"


def create_imgui_proxy(module: Any = _raw_imgui) -> ImguiProxy:
    """Create a wrapping proxy for ``module`` (defaults to imgui_bundle)."""
    return ImguiProxy(module)


imgui = create_imgui_proxy()

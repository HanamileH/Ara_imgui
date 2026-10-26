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


class _ChildContext:
    """``with imgui.child(...):`` -- wraps ``begin_child`` / ``end_child``.

    The object is truthy while the child is visible, so the body can be
    guarded with ``if child:`` when it is expensive to submit.
    """

    __slots__ = ("_module", "_args", "_kwargs", "visible")

    def __init__(self, module: Any, *args: Any, **kwargs: Any) -> None:
        self._module = module
        self._args = args
        self._kwargs = kwargs
        self.visible = False

    def __enter__(self) -> _ChildContext:
        self.visible = self._module.begin_child(*self._args, **self._kwargs)
        return self

    def __exit__(self, exc_type: Any, exc_value: Any, traceback: Any) -> bool:
        # EndChild() must always be called, even when BeginChild() returned
        # False (the child window is still pushed on the stack).
        self._module.end_child()
        return False

    def __bool__(self) -> bool:
        return bool(self.visible)

    def __repr__(self) -> str:
        return f"<imgui.child visible={self.visible}>"


class _TableContext:
    """``with imgui.table(...):`` -- legacy ImGui columns as a table.

    Wraps ``imgui.columns(..., borders)`` and the matching
    ``imgui.columns(1)``.  Headers are rendered as the first row.  Cells are
    submitted with ``imgui.next_column()``; the legacy API wraps to a new line
    after the last column, so rows need no explicit call.
    """

    __slots__ = ("_module", "_label", "_columns", "_headers", "_borders")

    def __init__(
        self,
        module: Any,
        label: str,
        columns: Any = None,
        headers: Any = None,
        borders: bool = True,
    ) -> None:
        if columns is None and headers is None:
            raise ValueError("Either columns or headers must be specified")

        if columns is None:
            columns = len(headers)

        if columns <= 0:
            raise ValueError("columns must be greater than zero")

        if headers is not None and len(headers) > columns:
            raise ValueError("Headers must be equal to or less than columns")

        self._module = module
        self._label = label
        self._columns = columns
        self._headers = list(headers) if headers is not None else None
        self._borders = borders

    def __enter__(self) -> _TableContext:
        module = self._module
        module.columns(self._columns, self._label, self._borders)

        if self._headers:
            for header in self._headers:
                module.text(header)
                module.next_column()

            for _ in range(self._columns - len(self._headers)):
                module.next_column()

            module.separator()

        return self

    def __exit__(self, exc_type: Any, exc_value: Any, traceback: Any) -> bool:
        # EndColumns() asserts when no columns are open; Columns(1) is the
        # safe, idempotent way to close the legacy columns set.
        self._module.columns(1)
        return False

    def __repr__(self) -> str:
        return f"<imgui.table columns={self._columns}>"


class _TreeContext:
    """``with imgui.tree(...):`` -- wraps ``tree_node`` / ``tree_pop``.

    ``TreePop()`` is only called when the node is open, and the object is
    truthy exactly in that case.  A collapsed node must not draw its content,
    so guard the body with ``if node:``::

        with imgui.tree("Settings") as node:
            if node:
                imgui.text("Advanced options")
    """

    __slots__ = ("_module", "_args", "_kwargs", "expanded")

    def __init__(self, module: Any, *args: Any, **kwargs: Any) -> None:
        self._module = module
        self._args = args
        self._kwargs = kwargs
        self.expanded = False

    def __enter__(self) -> _TreeContext:
        self.expanded = self._module.tree_node(*self._args, **self._kwargs)
        return self

    def __exit__(self, exc_type: Any, exc_value: Any, traceback: Any) -> bool:
        if self.expanded:
            self._module.tree_pop()
        return False

    def __bool__(self) -> bool:
        return bool(self.expanded)

    def __repr__(self) -> str:
        return f"<imgui.tree expanded={self.expanded}>"


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

    def child(self, *args: Any, **kwargs: Any) -> _ChildContext:
        """Context manager around ``begin_child`` / ``end_child``::

            with imgui.child("Log", size=imgui.ImVec2(0, 120)):
                imgui.text("Child content")
        """
        return _ChildContext(self._module, *args, **kwargs)

    def tree(self, *args: Any, **kwargs: Any) -> _TreeContext:
        """Context manager around ``tree_node`` / ``tree_pop``::

            with imgui.tree("Settings") as node:
                if node:
                    imgui.text("Advanced options")
        """
        return _TreeContext(self._module, *args, **kwargs)

    def table(
        self,
        label: str,
        columns: Any = None,
        headers: Any = None,
        borders: bool = True,
    ) -> _TableContext:
        """Context manager around the legacy ``columns`` API.

        ``columns`` defaults to the number of ``headers``.  When ``headers``
        is given, they are rendered as the first row.  Cells are submitted
        with ``imgui.next_column()``; the legacy API wraps to a new line after
        the last column, so no explicit row call is needed::

            with imgui.table("People", 3, ["Name", "Age", "Sex"]):
                for name, age, sex in people:
                    imgui.text(name)
                    imgui.next_column()
                    imgui.text(str(age))
                    imgui.next_column()
                    imgui.text(sex)
                    imgui.next_column()

        Positional arguments follow the ``label, columns, headers, borders``
        order.
        """
        return _TableContext(
            self._module, label, columns, headers, borders
        )

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
        return sorted(
            set(dir(module))
            | {"child", "is_item_changed", "raw", "table", "tree"}
        )

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

from __future__ import annotations
import functools
import warnings
from typing import Any, Callable, Dict, FrozenSet, NamedTuple, Tuple
from imgui_bundle import imgui as _raw_imgui

__all__ = [
    "CHANGED_WIDGETS",
    "LABEL_WIDGETS",
    "VALUE_SPECS",
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


# Widgets that take a label/ID as their first argument but do not return a
# value.  They get the same ``++`` counter handling as value widgets (which
# are covered by CHANGED_WIDGETS), so ``imgui.button("Delete++")`` works too.
LABEL_WIDGETS: FrozenSet[str] = frozenset(
    {
        # Buttons and selection
        "arrow_button",
        "button",
        "color_button",
        "invisible_button",
        "menu_item",
        "radio_button",
        "selectable",
        "small_button",

        # Trees and collapsing headers
        "collapsing_header",
        "tree_node",
        "tree_push",

        # Menus, popups, tabs, children, windows
        "begin",
        "begin_child",
        "begin_combo",
        "begin_list_box",
        "begin_menu",
        "begin_popup",
        "begin_popup_modal",
        "begin_tab_bar",
        "begin_tab_item",
        "begin_table",
        "open_popup",

        # Table columns
        "table_setup_column",
    }
)


class _ValueSpec(NamedTuple):
    """Where a widget keeps its value and what to start from.

    ``names``/``positions`` describe the value parameters in call order
    (``positions`` count the leading label as position 0).  ``default`` is a
    factory returning a fresh initial value, used only when the widget was
    never seen before and the caller did not pass ``default=``.
    """

    names: Tuple[str, ...]
    positions: Tuple[int, ...]
    default: Callable[[], Any]

    @property
    def count(self) -> int:
        return len(self.names)


def _int_default() -> int:
    return 0


def _float_default() -> float:
    return 0.0


def _int_list(size: int) -> Callable[[], list]:
    return lambda: [0] * size


def _float_list(size: int) -> Callable[[], list]:
    return lambda: [0.0] * size


# The value parameters of every wrapped widget.  Names must match the
# installed binding, because they are used when the value is passed as a
# keyword or omitted entirely.  Keeping the table explicit also gives each
# widget the right zero value (``""`` for text, ``0`` for a combo index, ...).
VALUE_SPECS: Dict[str, _ValueSpec] = {
    # Boolean inputs
    "checkbox": _ValueSpec(("v",), (1,), lambda: False),
    "checkbox_flags": _ValueSpec(("flags",), (1,), _int_default),

    # Colors
    "color_edit3": _ValueSpec(("col",), (1,), _float_list(3)),
    "color_edit4": _ValueSpec(("col",), (1,), lambda: [0.0, 0.0, 0.0, 1.0]),
    "color_picker3": _ValueSpec(("col",), (1,), _float_list(3)),
    "color_picker4": _ValueSpec(("col",), (1,), lambda: [0.0, 0.0, 0.0, 1.0]),

    # Selection
    "combo": _ValueSpec(("current_item",), (1,), _int_default),
    "list_box": _ValueSpec(("current_item",), (1,), _int_default),

    # Text
    "input_text": _ValueSpec(("str",), (1,), lambda: ""),
    "input_text_multiline": _ValueSpec(("str",), (1,), lambda: ""),
    # input_text_with_hint is the odd one out: the hint comes before the value.
    "input_text_with_hint": _ValueSpec(("str",), (2,), lambda: ""),

    # Integers
    "input_int": _ValueSpec(("v",), (1,), _int_default),
    "input_int2": _ValueSpec(("v",), (1,), _int_list(2)),
    "input_int3": _ValueSpec(("v",), (1,), _int_list(3)),
    "input_int4": _ValueSpec(("v",), (1,), _int_list(4)),
    "drag_int": _ValueSpec(("v",), (1,), _int_default),
    "drag_int2": _ValueSpec(("v",), (1,), _int_list(2)),
    "drag_int3": _ValueSpec(("v",), (1,), _int_list(3)),
    "drag_int4": _ValueSpec(("v",), (1,), _int_list(4)),
    "drag_int_range2": _ValueSpec(
        ("v_current_min", "v_current_max"), (1, 2), lambda: (0, 0)
    ),
    "slider_int": _ValueSpec(("v",), (1,), _int_default),
    "slider_int2": _ValueSpec(("v",), (1,), _int_list(2)),
    "slider_int3": _ValueSpec(("v",), (1,), _int_list(3)),
    "slider_int4": _ValueSpec(("v",), (1,), _int_list(4)),
    "v_slider_int": _ValueSpec(("v",), (2,), _int_default),

    # Floats
    "input_float": _ValueSpec(("v",), (1,), _float_default),
    "input_float2": _ValueSpec(("v",), (1,), _float_list(2)),
    "input_float3": _ValueSpec(("v",), (1,), _float_list(3)),
    "input_float4": _ValueSpec(("v",), (1,), _float_list(4)),
    "input_double": _ValueSpec(("v",), (1,), _float_default),
    "drag_float": _ValueSpec(("v",), (1,), _float_default),
    "drag_float2": _ValueSpec(("v",), (1,), _float_list(2)),
    "drag_float3": _ValueSpec(("v",), (1,), _float_list(3)),
    "drag_float4": _ValueSpec(("v",), (1,), _float_list(4)),
    "drag_float_range2": _ValueSpec(
        ("v_current_min", "v_current_max"), (1, 2), lambda: (0.0, 0.0)
    ),
    "slider_float": _ValueSpec(("v",), (1,), _float_default),
    "slider_float2": _ValueSpec(("v",), (1,), _float_list(2)),
    "slider_float3": _ValueSpec(("v",), (1,), _float_list(3)),
    "slider_float4": _ValueSpec(("v",), (1,), _float_list(4)),
    "slider_angle": _ValueSpec(("v_rad",), (1,), _float_default),
    "v_slider_float": _ValueSpec(("v",), (2,), _float_default),
}


_MISSING = object()


def _widget_id(label: Any) -> str:
    """Return the part of an ImGui label that makes up the widget ID.

    Dear ImGui hashes everything after ``##`` (or ``###``), so ``"Age##age"``
    and ``"Years##age"`` are the same widget and share their stored value.
    """
    text = str(label)
    if "##" in text:
        return text.rsplit("##", 1)[1]
    return text


def _stored_part(stored: Any, index: int, count: int) -> Any:
    """Pick one value out of a stored multi-value widget result."""
    if count == 1:
        return stored
    try:
        return stored[index]
    except (IndexError, KeyError, TypeError):
        return _MISSING


def _resolve_value_arguments(
    spec: _ValueSpec,
    values: Dict[str, Any],
    key: str,
    args: Tuple[Any, ...],
    kwargs: Dict[str, Any],
) -> Tuple[list, Dict[str, Any]]:
    """Fill omitted/``None`` widget values from the value memory."""
    args = list(args)
    defaults = kwargs.pop("default", _MISSING)
    stored = values.get(key, _MISSING)

    resolved = []
    for index, (name, position) in enumerate(zip(spec.names, spec.positions)):
        if len(args) > position:
            provided = args[position]
        elif name in kwargs:
            provided = kwargs.pop(name)
        else:
            provided = _MISSING

        if provided is not _MISSING and provided is not None:
            value = provided
        else:
            value = _MISSING

            if stored is not _MISSING:
                value = _stored_part(stored, index, spec.count)

            if value is _MISSING and defaults is not _MISSING and defaults is not None:
                value = _stored_part(defaults, index, spec.count)

            if value is _MISSING:
                value = _stored_part(spec.default(), index, spec.count)

        resolved.append(value)

    # Put the resolved values back where the binding expects them: replace an
    # existing positional argument or pass the value by keyword.
    for index, (name, position) in enumerate(zip(spec.names, spec.positions)):
        if len(args) > position:
            args[position] = resolved[index]
        else:
            kwargs[name] = resolved[index]

    return args, kwargs


_LABEL_ARGUMENT_NAMES: Tuple[str, ...] = ("label", "str_id", "name", "desc_id")


def _find_label(
    args: Tuple[Any, ...], kwargs: Dict[str, Any]
) -> Tuple[Any, Any]:
    """Return ``(label, keyword_name)`` for the first label-like argument.

    ``keyword_name`` is ``None`` when the label was passed positionally.
    ``label`` is ``_MISSING`` when no string label argument was found.
    """
    if args and isinstance(args[0], str):
        return args[0], None

    for name in _LABEL_ARGUMENT_NAMES:
        if name in kwargs and isinstance(kwargs[name], str):
            return kwargs[name], name

    return _MISSING, None


def _replace_label(
    args: Tuple[Any, ...],
    kwargs: Dict[str, Any],
    keyword_name: Any,
    label: str,
) -> Tuple[Tuple[Any, ...], Dict[str, Any]]:
    """Return call arguments with the label replaced."""
    if keyword_name is None:
        return (label,) + args[1:], kwargs

    kwargs = dict(kwargs)
    kwargs[keyword_name] = label
    return args, kwargs


def _wrap_label_widget(
    func: Callable[..., Any],
    name: str,
    proxy: ImguiProxy,
) -> Callable[..., Any]:
    """Wrap a label-taking widget so ``++`` labels get a frame counter."""

    @functools.wraps(func)
    def wrapper(*args: Any, **kwargs: Any) -> Any:
        label, keyword_name = _find_label(args, kwargs)
        if label is not _MISSING:
            expanded = proxy._expand_label(name, label)
            if expanded != label:
                args, kwargs = _replace_label(
                    args, kwargs, keyword_name, expanded
                )

        return func(*args, **kwargs)

    return wrapper


def _wrap_new_frame(
    func: Callable[..., Any],
    proxy: ImguiProxy,
) -> Callable[..., Any]:
    """Reset the ``++`` counters when a new frame starts."""

    @functools.wraps(func)
    def wrapper(*args: Any, **kwargs: Any) -> Any:
        result = func(*args, **kwargs)
        proxy._reset_label_counters()
        return result

    return wrapper


def _wrap_value_widget(
    func: Callable[..., Any],
    name: str,
    spec: _ValueSpec,
    values: Dict[str, Any],
    proxy: ImguiProxy,
) -> Callable[..., Any]:
    """Wrap one value widget so it remembers the value it returned."""

    @functools.wraps(func)
    def wrapper(*args: Any, **kwargs: Any) -> Any:
        label, keyword_name = _find_label(args, kwargs)
        if label is _MISSING:
            raise TypeError(
                f"{func.__name__}() missing required argument: 'label'"
            )

        expanded = proxy._expand_label(name, label)
        if expanded != label:
            args, kwargs = _replace_label(args, kwargs, keyword_name, expanded)

        key = _widget_id(expanded)
        args, kwargs = _resolve_value_arguments(spec, values, key, args, kwargs)
        value = unwrap_changed_result(func(*args, **kwargs))

        # Remember what the widget returned; the next frame uses it when the
        # caller omits the value or passes None.
        values[key] = value
        return value

    return wrapper


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

    Value widgets remember the value they returned, keyed by the widget ID
    (the part of the label after ``##``).  The value argument may therefore
    be omitted or passed as ``None`` -- the remembered value is reused.  When
    a value is passed, it replaces the remembered one.

    A label ending in ``++`` is expanded to a unique label using a per-label
    counter that restarts every frame, e.g. ``"Name++"`` becomes
    ``"Name##Name_0"`` on its first use and ``"Name##Name_1"`` on the second.
    Use ``\\++`` to get a literal trailing ``++``.
    """

    __slots__ = (
        "_module",
        "_cache",
        "_values",
        "_label_counters",
        "_counter_frame",
    )

    def __init__(self, module: Any = _raw_imgui) -> None:
        object.__setattr__(self, "_module", module)
        object.__setattr__(self, "_cache", {})
        object.__setattr__(self, "_values", {})
        object.__setattr__(self, "_label_counters", {})
        object.__setattr__(self, "_counter_frame", None)

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
                value = _wrap_value_widget(
                    attribute,
                    name,
                    VALUE_SPECS[name],
                    object.__getattribute__(self, "_values"),
                    self,
                )
            elif name in LABEL_WIDGETS:
                value = _wrap_label_widget(attribute, name, self)
            elif name == "new_frame":
                value = _wrap_new_frame(attribute, self)
            else:
                value = attribute

        cache[name] = value
        return value

    def _sync_label_counters(self) -> None:
        """Reset ``++`` counters when the underlying ImGui frame changes."""
        module = object.__getattribute__(self, "_module")
        getter = getattr(module, "get_frame_count", None)
        if getter is None:
            return

        try:
            frame = int(getter())
        except Exception:  # pragma: no cover - depends on the binding
            return

        if frame != object.__getattribute__(self, "_counter_frame"):
            object.__setattr__(self, "_counter_frame", frame)
            object.__getattribute__(self, "_label_counters").clear()

    def _reset_label_counters(self) -> None:
        counters = object.__getattribute__(self, "_label_counters")
        counters.clear()

        module = object.__getattribute__(self, "_module")
        getter = getattr(module, "get_frame_count", None)
        if getter is not None:
            try:
                object.__setattr__(self, "_counter_frame", int(getter()))
            except Exception:  # pragma: no cover - depends on the binding
                pass

    def _expand_label(self, widget: str, label: Any) -> Any:
        """Expand a trailing ``++`` into a per-label, per-frame counter ID."""
        if not isinstance(label, str) or not label.endswith("++"):
            return label

        # ``\++`` is the escape sequence: a literal trailing ``++``.
        if label.endswith("\\++"):
            return label[:-3] + "++"

        self._sync_label_counters()
        counters = object.__getattribute__(self, "_label_counters")

        base = label[:-2]
        index = counters.get(base, 0)
        counters[base] = index + 1

        if "##" in base:
            warnings.warn(
                f"ara_imgui: label {label!r} ends with '++' and also contains "
                "'##'. The counter is appended to the explicit ID; use either "
                "'++' or an explicit ID, not both.",
                UserWarning,
                stacklevel=3,
            )
            return f"{base}_{index}"

        if widget in CHANGED_WIDGETS:
            warnings.warn(
                f"ara_imgui: label {label!r} ends with '++' and is used with "
                f"the stateful widget {widget!r}. Per-frame counter IDs can "
                "move remembered values between items when the order changes; "
                "pass an explicit ID instead.",
                UserWarning,
                stacklevel=3,
            )

        return f"{base}##{base}_{index}"
    def child(self, *args: Any, **kwargs: Any) -> _ChildContext:
        """Context manager around ``begin_child`` / ``end_child``::

            with imgui.child("Log", size=imgui.ImVec2(0, 120)):
                imgui.text("Child content")
        """
        return _ChildContext(self, *args, **kwargs)

    def tree(self, *args: Any, **kwargs: Any) -> _TreeContext:
        """Context manager around ``tree_node`` / ``tree_pop``::

            with imgui.tree("Settings") as node:
                if node:
                    imgui.text("Advanced options")
        """
        return _TreeContext(self, *args, **kwargs)

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
            self, self._expand_label("table", label), columns, headers, borders
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

    def set_item_value(self, id: Any, value: Any) -> None:
        """Set the remembered value of the widget with the given ID.

        ``id`` is the widget ID -- the part of the label after ``##`` -- or
        the whole label.  The value is used the next time that widget's value
        argument is omitted or passed as ``None``::

            imgui.set_item_value("Age##input_id", 18)
            age = imgui.input_int("Age##input_id")

        No ImGui item is touched: this only changes what the widget will use
        the next time it is submitted without a value.  Passing ``None``
        forgets the remembered value, making the widget fall back to its
        ``default=`` (or its zero value) on the next frame.
        """
        if id is None:
            raise ValueError("id must not be None")

        values = object.__getattribute__(self, "_values")
        key = _widget_id(id)
        if value is None:
            values.pop(key, None)
        else:
            values[key] = value

    def __dir__(self) -> list:
        module = object.__getattribute__(self, "_module")
        return sorted(
            set(dir(module))
            | {
                "child",
                "is_item_changed",
                "raw",
                "set_item_value",
                "table",
                "tree",
            }
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

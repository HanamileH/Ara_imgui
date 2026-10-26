# Type hints for the public ``ara_imgui.imgui`` module.
#
# ``from imgui_bundle.imgui import *`` re-exports the untouched API; the
# definitions below override the parts Ara_imgui changes.  The wrapped widget
# signatures are derived from imgui_bundle's own stub with ``(changed, value)``
# reduced to the value.  Keep them in sync with ``CHANGED_WIDGETS`` in
# ``_imgui.py`` -- tests check that every wrapped name is declared here.
from types import ModuleType
from typing import Any, List, Optional, Tuple, overload

from imgui_bundle.imgui import *  # type: ignore


def checkbox(label: str, v: bool) -> bool:
    ...

def checkbox_flags(label: str, flags: int, flags_value: int) -> int:
    ...

@overload
def combo(label: str, current_item: int, items: List[str], popup_max_height_in_items: int=-1) -> int:
    ...

@overload
def combo(label: str, current_item: int, items_separated_by_zeros: str, popup_max_height_in_items: int=-1) -> int:
    ...

def drag_float(label: str, v: float, v_speed: float=1.0, v_min: float=0.0, v_max: float=0.0, format: str='%.3', flags: SliderFlags=0) -> float:
    ...

def drag_float2(label: str, v: List[float], v_speed: float=1.0, v_min: float=0.0, v_max: float=0.0, format: str='%.3', flags: SliderFlags=0) -> List[float]:
    ...

def drag_float3(label: str, v: List[float], v_speed: float=1.0, v_min: float=0.0, v_max: float=0.0, format: str='%.3', flags: SliderFlags=0) -> List[float]:
    ...

def drag_float4(label: str, v: List[float], v_speed: float=1.0, v_min: float=0.0, v_max: float=0.0, format: str='%.3', flags: SliderFlags=0) -> List[float]:
    ...

def drag_float_range2(label: str, v_current_min: float, v_current_max: float, v_speed: float=1.0, v_min: float=0.0, v_max: float=0.0, format: str='%.3', format_max: Optional[str]=None, flags: SliderFlags=0) -> Tuple[float, float]:
    ...

def drag_int(label: str, v: int, v_speed: float=1.0, v_min: int=0, v_max: int=0, format: str='%d', flags: SliderFlags=0) -> int:
    ...

def drag_int2(label: str, v: List[int], v_speed: float=1.0, v_min: int=0, v_max: int=0, format: str='%d', flags: SliderFlags=0) -> List[int]:
    ...

def drag_int3(label: str, v: List[int], v_speed: float=1.0, v_min: int=0, v_max: int=0, format: str='%d', flags: SliderFlags=0) -> List[int]:
    ...

def drag_int4(label: str, v: List[int], v_speed: float=1.0, v_min: int=0, v_max: int=0, format: str='%d', flags: SliderFlags=0) -> List[int]:
    ...

def drag_int_range2(label: str, v_current_min: int, v_current_max: int, v_speed: float=1.0, v_min: int=0, v_max: int=0, format: str='%d', format_max: Optional[str]=None, flags: SliderFlags=0) -> Tuple[int, int]:
    ...

def slider_float(label: str, v: float, v_min: float, v_max: float, format: str='%.3', flags: SliderFlags=0) -> float:
    ...

@overload
def slider_float2(label: str, v: List[float], v_min: float, v_max: float, format: str='%.3', flags: SliderFlags=0) -> List[float]:
    ...

@overload
def slider_float2(label: str, v: ImVec2Like, v_min: float, v_max: float, format: str='%.3', flags: SliderFlags=0) -> ImVec2:
    ...

def slider_float3(label: str, v: List[float], v_min: float, v_max: float, format: str='%.3', flags: SliderFlags=0) -> List[float]:
    ...

@overload
def slider_float4(label: str, v: List[float], v_min: float, v_max: float, format: str='%.3', flags: SliderFlags=0) -> List[float]:
    ...

@overload
def slider_float4(label: str, v: ImVec4Like, v_min: float, v_max: float, format: str='%.3', flags: SliderFlags=0) -> ImVec4:
    ...

def slider_angle(label: str, v_rad: float, v_degrees_min: float=-360.0, v_degrees_max: float=+360.0, format: str='%.0 deg', flags: SliderFlags=0) -> float:
    ...

def slider_int(label: str, v: int, v_min: int, v_max: int, format: str='%d', flags: SliderFlags=0) -> int:
    ...

def slider_int2(label: str, v: List[int], v_min: int, v_max: int, format: str='%d', flags: SliderFlags=0) -> List[int]:
    ...

def slider_int3(label: str, v: List[int], v_min: int, v_max: int, format: str='%d', flags: SliderFlags=0) -> List[int]:
    ...

def slider_int4(label: str, v: List[int], v_min: int, v_max: int, format: str='%d', flags: SliderFlags=0) -> List[int]:
    ...

def v_slider_float(label: str, size: ImVec2Like, v: float, v_min: float, v_max: float, format: str='%.3', flags: SliderFlags=0) -> float:
    ...

def v_slider_int(label: str, size: ImVec2Like, v: int, v_min: int, v_max: int, format: str='%d', flags: SliderFlags=0) -> int:
    ...

def input_float(label: str, v: float, step: float=0.0, step_fast: float=0.0, format: str='%.3', flags: InputTextFlags=0) -> float:
    ...

@overload
def input_float2(label: str, v: List[float], format: str='%.3', flags: InputTextFlags=0) -> List[float]:
    ...

@overload
def input_float2(label: str, v: ImVec2Like, format: str='%.3', flags: InputTextFlags=0) -> ImVec2:
    ...

def input_float3(label: str, v: List[float], format: str='%.3', flags: InputTextFlags=0) -> List[float]:
    ...

@overload
def input_float4(label: str, v: List[float], format: str='%.3', flags: InputTextFlags=0) -> List[float]:
    ...

@overload
def input_float4(label: str, v: ImVec4Like, format: str='%.3', flags: InputTextFlags=0) -> ImVec4:
    ...

def input_int(label: str, v: int, step: int=1, step_fast: int=100, flags: InputTextFlags=0) -> int:
    ...

def input_int2(label: str, v: List[int], flags: InputTextFlags=0) -> List[int]:
    ...

def input_int3(label: str, v: List[int], flags: InputTextFlags=0) -> List[int]:
    ...

def input_int4(label: str, v: List[int], flags: InputTextFlags=0) -> List[int]:
    ...

def input_double(label: str, v: float, step: float=0.0, step_fast: float=0.0, format: str='%.6', flags: InputTextFlags=0) -> float:
    ...

@overload
def color_edit3(label: str, col: List[float], flags: ColorEditFlags=0) -> List[float]:
    ...

@overload
def color_edit3(label: str, col: ImVec4Like, flags: ColorEditFlags=0) -> ImVec4:
    ...

@overload
def color_edit4(label: str, col: List[float], flags: ColorEditFlags=0) -> List[float]:
    ...

@overload
def color_edit4(label: str, col: ImVec4Like, flags: ColorEditFlags=0) -> ImVec4:
    ...

@overload
def color_picker3(label: str, col: List[float], flags: ColorEditFlags=0) -> List[float]:
    ...

@overload
def color_picker3(label: str, col: ImVec4Like, flags: ColorEditFlags=0) -> ImVec4:
    ...

@overload
def color_picker4(label: str, col: List[float], flags: ColorEditFlags=0, ref_col: Optional[float]=None) -> List[float]:
    ...

@overload
def color_picker4(label: str, col: ImVec4Like, flags: ColorEditFlags=0, ref_col: Optional[ImVec4Like]=None) -> ImVec4:
    ...

def list_box(label: str, current_item: int, items: List[str], height_in_items: int=-1) -> int:
    ...

def input_text(label: str, str: str, flags: InputTextFlags=0, callback: InputTextCallback=None, user_data: Optional[Any]=None) -> str:
    ...

def input_text_multiline(label: str, str: str, size: Optional[ImVec2Like]=None, flags: InputTextFlags=0, callback: InputTextCallback=None, user_data: Optional[Any]=None) -> str:
    ...

def input_text_with_hint(label: str, hint: str, str: str, flags: InputTextFlags=0, callback: InputTextCallback=None, user_data: Optional[Any]=None) -> str:
    ...


class _ChildContext:
    visible: bool
    def __enter__(self) -> _ChildContext: ...
    def __exit__(self, exc_type: Any, exc_value: Any, traceback: Any) -> bool: ...
    def __bool__(self) -> bool: ...


class _TableContext:
    def __enter__(self) -> _TableContext: ...
    def __exit__(self, exc_type: Any, exc_value: Any, traceback: Any) -> bool: ...


class _TreeContext:
    expanded: bool
    def __enter__(self) -> _TreeContext: ...
    def __exit__(self, exc_type: Any, exc_value: Any, traceback: Any) -> bool: ...
    def __bool__(self) -> bool: ...


@overload
def child(str_id: str, size: Optional[ImVec2Like] = None, child_flags: ChildFlags = 0, window_flags: WindowFlags = 0) -> _ChildContext: ...
@overload
def child(id_: ID, size: Optional[ImVec2Like] = None, child_flags: ChildFlags = 0, window_flags: WindowFlags = 0) -> _ChildContext: ...


def table(label: str, columns: Optional[int] = None, headers: Optional[List[str]] = None, borders: bool = True) -> _TableContext: ...


@overload
def tree(label: str) -> _TreeContext: ...
@overload
def tree(str_id: str, fmt: str) -> _TreeContext: ...
@overload
def tree(ptr_id: Any, fmt: str) -> _TreeContext: ...


def is_item_changed() -> bool: ...


raw: ModuleType

"""The public ``ara_imgui.imgui`` module.

Every function, type and constant from :mod:`imgui_bundle.imgui` is
re-exported unchanged, then the parts Ara_imgui customizes are overridden:

- value widgets return the new value instead of ``(changed, value)``; read the
  flag with :func:`is_item_changed`;
- :func:`child`, :func:`table` and :func:`tree` are context managers;
- :data:`raw` points at the untouched ``imgui_bundle.imgui`` module.

Type hints for the whole module live in the sibling ``imgui.pyi``, so IDE
completion and signatures match this module's actual API.
"""

from imgui_bundle.imgui import *  # noqa: F401,F403

from ._imgui import CHANGED_WIDGETS as _CHANGED_WIDGETS
from ._imgui import imgui as _proxy

for _widget in _CHANGED_WIDGETS:
    globals()[_widget] = getattr(_proxy, _widget)
del _widget

child = _proxy.child
table = _proxy.table
tree = _proxy.tree
is_item_changed = _proxy.is_item_changed
raw = _proxy.raw

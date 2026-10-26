"""Tests for the ``imgui.child`` / ``imgui.table`` / ``imgui.tree`` managers.

The tests drive a real (headless) ImGui context: that is the only way to
verify that ``EndChild`` / ``EndTable`` / ``TreePop`` are called in a matching
way -- a missed call trips an assertion on the following frame.
"""

from imgui_bundle import imgui as raw_imgui

from ara_imgui import imgui

_context_ready = False


def _ensure_context():
    global _context_ready
    if _context_ready:
        return

    imgui.create_context()
    io = imgui.get_io()
    io.display_size = (800, 600)
    io.delta_time = 1 / 60
    io.backend_flags |= raw_imgui.BackendFlags_.renderer_has_textures
    _context_ready = True


def _run_frame(body):
    _ensure_context()
    imgui.new_frame()
    imgui.set_next_window_pos(imgui.ImVec2(0, 0))
    imgui.begin("test window")
    try:
        body()
    finally:
        imgui.end()
    imgui.render()


def test_child_context_manager():
    state = {}

    def body():
        with imgui.child("child", size=imgui.ImVec2(200, 80)) as child:
            state["visible"] = bool(child)
            imgui.text("inside the child")

    _run_frame(body)
    assert state["visible"] is True


def test_child_context_manager_ends_child_on_every_frame():
    def body():
        with imgui.child("child, reused"):
            imgui.text("content")

    # A missing EndChild() would trip ImGui on the second frame.
    _run_frame(body)
    _run_frame(body)


def test_table_infers_columns_from_headers():
    state = {}

    def body():
        with imgui.table("people", headers=["Name", "Age", "Sex"]):
            state["columns"] = imgui.get_columns_count()
            state["column"] = imgui.get_column_index()

            imgui.text("John")
            imgui.next_column()
            imgui.text("25")
            imgui.next_column()
            imgui.text("Male")
            imgui.next_column()

            # next_column() wraps to the first column of the next row.
            state["wrapped_column"] = imgui.get_column_index()

    _run_frame(body)
    assert state == {"columns": 3, "column": 0, "wrapped_column": 0}


def test_table_accepts_explicit_columns():
    state = {}

    def body():
        with imgui.table("without headers", 2):
            state["columns"] = imgui.get_columns_count()

            imgui.text("a")
            imgui.next_column()
            imgui.text("b")
            imgui.next_column()

    _run_frame(body)
    assert state["columns"] == 2


def test_table_closes_columns_after_body():
    state = {}

    def body():
        with imgui.table("closed after body", 2):
            imgui.text("a")
            imgui.next_column()
            imgui.text("b")

        state["columns_after"] = imgui.get_columns_count()

    _run_frame(body)
    assert state["columns_after"] == 1


def test_table_requires_columns_or_headers():
    try:
        imgui.table("no columns")
    except ValueError:
        pass
    else:
        raise AssertionError("expected ValueError")


def test_table_rejects_too_many_headers():
    try:
        imgui.table("too many headers", 2, ["a", "b", "c"])
    except ValueError:
        pass
    else:
        raise AssertionError("expected ValueError")


def test_table_rejects_non_positive_columns():
    try:
        imgui.table("no columns", 0)
    except ValueError:
        pass
    else:
        raise AssertionError("expected ValueError")


def test_tree_open_and_closed_nodes():
    state = {}

    def body():
        with imgui.tree("closed node") as node:
            state["closed"] = bool(node)
            if node:
                imgui.text("not drawn")

        imgui.set_next_item_open(True)
        with imgui.tree("open node") as node:
            state["open"] = bool(node)
            if node:
                imgui.text("drawn")

    _run_frame(body)
    assert state == {"closed": False, "open": True}


def test_tree_context_manager_balances_tree_stack():
    def body():
        imgui.set_next_item_open(True)
        with imgui.tree("reused open node") as node:
            if node:
                imgui.text("content")

    # A misplaced or missing TreePop() would trip ImGui on the second frame.
    _run_frame(body)
    _run_frame(body)


def test_proxy_exposes_context_managers():
    assert "child" in dir(imgui)
    assert "table" in dir(imgui)
    assert "tree" in dir(imgui)
    assert callable(imgui.child)
    assert callable(imgui.table)
    assert callable(imgui.tree)

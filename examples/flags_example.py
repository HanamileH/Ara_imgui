from ara_imgui import App, flags, imgui

app = App("Flags example", 480, 420)

volume = 50
amount = "100"

def gui():
    global volume, amount

    # only digits are accepted in this field
    imgui.text("flags.input_text")
    amount = imgui.input_text(
        "Amount",
        amount,
        flags=flags.input_text.chars_decimal,
    )

    imgui.separator()

    # logarithmic scale is handy for wide ranges
    imgui.text("flags.slider")
    volume = imgui.slider_int(
        "Volume",
        volume,
        1,
        1000,
        flags=flags.slider.logarithmic,
    )

    imgui.separator()

    # the node starts open and takes the whole row
    imgui.text("flags.tree_node")
    if imgui.tree_node_ex(
        "Advanced",
        flags.tree_node.default_open | flags.tree_node.span_avail_width,
    ):
        imgui.text("Opened by default and spans the full width")
        imgui.tree_pop()

    imgui.separator()

    # a child region with a border
    imgui.text("flags.child")
    with imgui.child(
        "bordered child",
        size=imgui.ImVec2(0, 60),
        child_flags=flags.child.borders,
    ):
        imgui.text("Child with flags.child.borders")

    imgui.separator()

app.run(gui)

from ara_imgui import App, imgui

app = App("Imgui Example", 500, 800)

checkboxs = [True, False, False]
radio_selected = 0
text_input = "Michail"
int_val = 50
float_val = 0.5
combo_selected = 0
color = [1.0, 0.5, 0.0]

def gui():
    global radio_selected, text_input
    global int_val, float_val
    global combo_selected, color
    
    # Text
    imgui.text("This is a text")
    imgui.text("Hello, world!")
    
    # Separator
    imgui.separator()

    # Buttons, same_line and tooltips
    if imgui.button("Button 1"):
        print("Button 1 clicked")
    
    if imgui.is_item_hovered():
        imgui.set_tooltip("This is a tooltip text")
    
    imgui.same_line()
        
    if imgui.button("Button 2"):
        print("Button 2 clicked")
        
    imgui.same_line()
        
    if imgui.button("Button 3"):
        print("Button 3 clicked")
    
    imgui.separator()
    
    # Checkbox
    checkboxs[0] = imgui.checkbox("Checkbox 1", checkboxs[0])
    checkboxs[1] = imgui.checkbox("Checkbox 2", checkboxs[1])
    checkboxs[2] = imgui.checkbox("Checkbox 3", checkboxs[2])

    imgui.separator()
    
    # Radio buttons
    if imgui.radio_button("Radio 1", radio_selected == 0):
        radio_selected = 0
        print("Radio 1 clicked")

    if imgui.radio_button("Radio 2", radio_selected == 1):
        radio_selected = 1
        print("Radio 2 clicked")
        
    if imgui.radio_button("Radio 3", radio_selected == 2):
        radio_selected = 2
        print("Radio 3 clicked")

    imgui.separator()
    
    # Text input
    # Widgets return the new value; is_item_changed() reports the edit flag.
    text_input = imgui.input_text("Text Input", text_input)

    if imgui.is_item_changed():
        print("Text input changed")
    
    imgui.text(f"Hello, {text_input if text_input else 'unknown'}!")
    
    imgui.separator()
    
    # Number input
    int_val = imgui.input_int("Int input", int_val)
    float_val = imgui.input_float("Float input", float_val)
    
    imgui.separator()
    
    # Sliders
    int_val = imgui.slider_int("Slider int", int_val, 0, 100)
    float_val = imgui.slider_float("Slider float", float_val, 0.0, 1.0)
    
    imgui.separator()
    
    # Progressbar
    imgui.text("Progress:")
    imgui.progress_bar(float_val)
    
    imgui.separator()
    
    # Combo box
    combo_selected = imgui.combo("Combo", combo_selected, ["Option 1", "Option 2", "Option 3"])
    
    imgui.text(f"Selected option: {combo_selected}")
    
    imgui.separator()
    
    # Color picker
    color = imgui.color_edit3("Color picker", color)
    
    imgui.separator()
    
    # Child
    with imgui.child("Child", size=imgui.ImVec2(0, 70)):
        imgui.text("This is a child")
        imgui.text("Hello, world!")

        for i in range(10):
            imgui.text(f"Child text {i}")
        
    imgui.separator()
    
    # Tree Node
    with imgui.tree("Tree node 1") as node:
        if node:
            imgui.button("Child 1")

            with imgui.tree("Child 2") as child:
                if child:
                    imgui.button("Child 2")
                    imgui.button("Child 3")

            with imgui.tree("Child 3") as child:
                if child:
                    imgui.button("Child 4")
                    imgui.button("Child 5")
                    imgui.button("Child 6")

    imgui.separator()
    
    # Table
    with imgui.table("##table columns", 5):
        # Rows
        for i in range(4):
            # Columns
            for j in range(5):
                imgui.text(f"item {i} {j}")
                imgui.next_column()


app.run(gui)

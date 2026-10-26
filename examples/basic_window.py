from ara_imgui import App, imgui

app = App("Basic Window")

name = ""
def gui():
   global name
   imgui.text("Example of a basic window")

   name = imgui.input_text("Enter your name", name)

   if imgui.is_item_changed():
      print(f"Input text: {name}")

   imgui.text(f"Hello, {name if name else 'Unknown'}!")


app.run(gui)

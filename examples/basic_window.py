from ara_imgui import App, imgui

app = App("Basic Window")

name = ""
def gui():
   global name
   imgui.text("Example of a basic window")

   changed, name = imgui.input_text("Enter your name", name)

   if changed:
      print(f"Input text: {name}")

   imgui.text(f"Hello, {name if name else "Unknown"}!")


app.run(gui)
from ara_imgui import App, imgui

app = App("Table example")

people = [
   ("John", 25, "Male"),
   ("Jane", 30, "Female"),
   ("Alex", 19, "Male"),
   ("Maria", 41, "Female"),
]

def gui():
   imgui.text("Table example")

   with imgui.table("Table", headers=["Name", "Age", "Sex"]):
      for name, age, sex in people:
         imgui.text(name)
         imgui.next_column()

         imgui.text(str(age))
         imgui.next_column()

         imgui.text(sex)
         imgui.next_column()

app.run(gui)

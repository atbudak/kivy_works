import kivy
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.properties import ObjectProperty

# Essentially we use the kivy language to separate style with python code


class MyGrid(Widget):
    name = ObjectProperty(None)
    lastname = ObjectProperty(None)
    email = ObjectProperty(None)

    def btn(self):
        print(self.name.text, self.lastname.text, self.email.text)
        self.name.text = ""
        self.lastname.text = ""
        self.email.text = ""


class MyApp(App):
    def build(self):
        return MyGrid()


if __name__ == "__main__":
    MyApp().run()

from kivy.app import App
from kivy.lang import Builder
from kivy.core.window import Window

class MilesKilometresApp:
    def build(self):
        Window.size = (400, 200)
        self.title = "Convert Miles to Kilometres"
        self.root = Builder.load_file('convert_miles_km.kv')
        return self.root

#    def handle_calculate(self, value):


MilesKilometresApp().run()


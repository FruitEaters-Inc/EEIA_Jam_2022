import Map
from kivy.core.window import Window
from kivy.uix.relativelayout import RelativeLayout
from kivy.app import App
import kivy

kivy.require('2.0.0')
Window.size = (1920, 1080)
Window.clearcolor = (78 / 255, 173 / 255, 245 / 255, 1)


# Window.fullscreen = True


class MyApp(App):
    def __init__(self):
        super().__init__()

        self.map = None
        self.tile_map = None

        self.layout = None

    def build(self):
        self.map = Map.load_map("map.txt")
        self.tile_map = Map.map_isometrise(self.map)

        self.layout = RelativeLayout()

        Map.build_map(self.tile_map, self.layout)

        return self.layout


MyApp().run()

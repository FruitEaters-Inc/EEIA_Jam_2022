from kivy.uix.image import Image
from kivy.uix.button import Button


class Event:
    def __init__(self, tile):
        self.tile = tile
        self.target = None
        self.image = Image(source='alert.zip', pos=tile.pos, nocache=True)
        self.button = Button(background_normal='drone.png', background_down='drone.png', pos=tile.pos,
                             size_hint=(None, None), size=(40, 40))
        self.button.bind(on_press=lambda instance: self.print())

    def draw_event(self, layout):
        layout.add_widget(self.image)
        layout.add_widget(self.button)

    def print(self):
        print("nie dzila")

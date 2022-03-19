import random

from kivy.uix.image import Image
from kivy.uix.button import Button


class Event:
    def __init__(self, tile):
        self.tile = tile
        self.target = None
        self.image = Image(source='alert.zip', pos=tile.pos, nocache=True)
        x = tile.pos[0]
        y = tile.pos[1]
        x += 940
        y += 520

        self.random_package()

        self.button = Button(background_normal='trans.png', background_down='trans.png', pos=(x, y),
                             size_hint=(None, None), size=(40, 40))
        self.button.bind(on_press=lambda instance: self.print())

    def draw_event(self, layout):
        layout.add_widget(self.image)
        layout.add_widget(self.button)

    def print(self):
        print("nie dzila")

    def random_package(self):
        packages = ["aid_kit", "ice_cream"]
        self.target = random.choice(packages)

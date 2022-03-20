import random

from kivy.uix.image import Image
from kivy.uix.button import Button

destinations = []


def add_destination(event):
    global destinations
    destinations.append(event)


def get_destinations():
    global destinations
    return destinations


class Event:
    def __init__(self, tile):
        self.obsolete = False
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
        self.button.bind(on_press=lambda instance: add_destination(self))

    def draw_event(self, layout):
        if self.image is not None:
            layout.add_widget(self.image)
        if self.button is not None:
            layout.add_widget(self.button)

    def random_package(self):
        packages = ["aid_kit", "ice_cream"]
        self.target = random.choice(packages)

    def remove_button(self):
        self.button = None

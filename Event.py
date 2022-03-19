from kivy.uix.image import Image


class Event:
    def __init__(self, tile):
        self.tile = tile
        self.target = None
        self.image = Image(source='alert.zip', pos=tile.pos, nocache=True)

    def draw_event(self, layout):
        layout.clear_widgets()
        layout.add_widget(self.image)

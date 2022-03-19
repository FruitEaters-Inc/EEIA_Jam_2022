from Tile import Tile
from kivy.uix.image import Image


class Drone:
    def __init__(self, tile, drone_range: int):
        self.current_tile = tile
        self.current_pos = self.current_tile.pos
        self.range = drone_range
        self.movePath = []
        self.image = Image(source='drone.png', pos=self.current_pos, nocache=True)

    def pop_move(self):
        if len(self.movePath) == 0:
            return
        target = self.movePath[0]
        self.move_to(target)

    def move_to(self, target: Tile):
        if not target.is_neighbour(self.current_tile):
            return
        self.current_tile = target
        self.current_pos = target.pos
        target.get_interaction()

    def move_direction(self, direction: str) -> None:
        if direction in self.current_tile.neighbours.keys():
            self.move_to(self.current_tile.neighbours[direction])\


    def draw_drone(self, layout):
        layout.add_widget(self.image)


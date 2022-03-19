from Tile import Tile
from kivy.uix.image import Image

from pathfinding import dfs


class Drone:
    def __init__(self, tile, drone_range: int):
        self.current_tile = tile
        self.current_pos = self.current_tile.pos
        self.range = drone_range
        self.movePath = []
        self.targets = []
        self.image = Image(source='drone.zip', pos=self.current_pos, nocache=True)

    def set_image(self, image: str):
        self.image = Image(source=image, pos=self.current_pos, nocache=True)

    def add_target(self, target: Tile):
        self.targets.append(target)

    def create_path(self, target: Tile):
        path = dfs(self.current_tile, target)
        self.movePath = path + path[::-1]

    def pop_move(self):
        if len(self.movePath) == 0:
            return
        return self.movePath.pop()

    def move_to(self, target: Tile):
        if target is None:
            return
        if not target.is_neighbour(self.current_tile):
            return
        self.current_tile = target
        self.current_pos = target.pos
        self.image.pos = target.pos
        target.get_interaction()

    def move_direction(self, direction: str) -> None:
        if direction in self.current_tile.neighbours.keys():
            self.move_to(self.current_tile.neighbours[direction])

    def draw_drone(self, layout):
        layout.add_widget(self.image)


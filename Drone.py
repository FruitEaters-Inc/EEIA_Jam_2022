from Event import Event
from Tile import Tile
from kivy.uix.image import Image

from pathfinding import dfs


class Drone:
    # Replace tile argument with event?
    def __init__(self, tile, drone_range: int):
        self.current_tile = tile
        self.current_pos = self.current_tile.pos
        self.range = drone_range
        self.movePath = []
        self.imagePath = []
        self.targets = []
        self.image = Image(source='drone.zip', pos=self.current_pos,
                           nocache=True)

    def set_image(self, image: str):
        if self.image.source == image:
            return

        if image == "aid_kit":
            self.image.source = "drone_med.zip"
        elif image == "ice_cream":
            self.image.source = "drone_ice.zip"
        elif image == "empty":
            self.remove_event()
            self.image.source = "drone.zip"

    def remove_event(self):
        if len(self.targets) != 0:
            # Removes the event from self.targets and marks it as obsolete
            self.targets.pop(0).obsolete = True

    def add_target(self, target: Event):
        self.targets.append(target)

    def create_path(self, target: Tile, package: str):
        path = dfs(self.current_tile, target)
        self.movePath = path + path[::-1]
        self.imagePath = ["empty"] * len(path) + [package] * len(path)

    def pop_move(self):
        if len(self.movePath) == 0:
            return
        self.set_image(self.imagePath.pop())
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

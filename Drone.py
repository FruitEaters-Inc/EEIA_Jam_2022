from Tile import Tile
from kivy.uix.image import Image


class Drone:
    def __init__(self, tile, drone_range: int):
        self.current_tile = tile
        self.current_pos = self.current_tile.pos
        self.range = drone_range
        self.movePath = []
        self.targets = []
        self.image = Image(source='drone.zip', pos=self.current_pos, nocache=True)

    def add_target(self, target: Tile):
        self.targets.append(target)

    def navigate_to(self, target: Tile):
        # find_path()
        # movePath.append(path)
        # movePath.append(path[::-1])
            # Of course there'd have to be a delay between each move
        # while len(self.movePath) != 0:
        #     self.pop_move()
        pass

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
        self.image.pos = target.pos
        target.get_interaction()

    def move_direction(self, direction: str) -> None:
        if direction in self.current_tile.neighbours.keys():
            self.move_to(self.current_tile.neighbours[direction])

    def draw_drone(self, layout):
        layout.clear_widgets()
        layout.add_widget(self.image)


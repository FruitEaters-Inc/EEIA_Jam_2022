from Tile import Tile


class Drone:
    def __init__(self, start_pos: (int, int), range: int, tileMap):
        self.start_pos = start_pos
        self.current_pos = start_pos
        self.current_tile = tileMap[start_pos[0]][start_pos[1]]
        self.range = range
        self.movePath = []

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



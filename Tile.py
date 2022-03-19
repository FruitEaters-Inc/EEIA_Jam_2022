def check_up(tile, tile_map, x, y):
    tile.neighbours['up'] = tile_map[y-1][x]


def check_down(tile, tile_map, x, y):
    tile.neighbours['down'] = tile_map[y+1][x]


def check_right(tile, tile_map, x, y):
    tile.neighbours['right'] = tile_map[y][x+1]


def check_left(tile, tile_map, x, y):
    tile.neighbours['left'] = tile_map[y][x-1]


def find_neighbours(tile_map):
    max_x, max_y = len(tile_map[0]) - 1, len(tile_map) - 1
    for y, row in enumerate(tile_map):
        for x, tile in enumerate(row):
            if y != 0:
                check_up(tile, tile_map, x, y)
            if y != max_y:
                check_down(tile, tile_map, x, y)
            if x != 0:
                check_left(tile, tile_map, x, y)
            if x != max_x:
                check_right(tile, tile_map, x, y)



class Tile:
    def __init__(self):
        self.pos = None
        self.neighbours = {}
        self.image = None
        self.is_safe = None
        self.is_permitted = None

    def get_interaction(self):
        pass
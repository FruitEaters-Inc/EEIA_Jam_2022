from kivy.uix.image import Image

import Tile


def load_map(file):
    f = open(file)

    map_data = []

    for row in f.read().split('\n'):
        map_row = [c for c in row]
        map_data.append(map_row)

    f.close()
    return map_data


def map_organise(char_map):
    tile_map = []
    tile_row = []
    y_counter = 0

    for y in char_map:

        y_coord = y_counter * -40 + 520
        x_counter = 0

        for x in y:

            new_tile = Tile.Tile()

            x_coord = x_counter * 40 - 940

            if x == '1':
                new_tile.image = Image(source='road.png', pos=(x_coord, y_coord), nocache=True)
                new_tile.is_safe = True
                new_tile.is_permitted = True
            elif x == '0':
                new_tile.image = Image(source='grass.png', pos=(x_coord, y_coord), nocache=True)
                new_tile.is_safe = True
                new_tile.is_permitted = True

            new_tile.pos = (x_coord, y_coord)

            x_counter += 1

            tile_row.append(new_tile)

        tile_map.append(tile_row.copy())
        tile_row.clear()

        y_counter += 1

    return tile_map


def build_map(tile_map, layout):
    for row in tile_map:
        for tile in row:
            if tile is not None and tile.image is not None:
                layout.add_widget(tile.image)

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

            if 'a' <= x <= 'q':
                new_tile.is_safe = True
                new_tile.is_permitted = True

            if x == 'a':
                new_tile.image = Image(source='roads/a.png', pos=(x_coord, y_coord), nocache=True)
            elif x == 'b':
                new_tile.image = Image(source='roads/b.png', pos=(x_coord, y_coord), nocache=True)
            elif x == 'c':
                new_tile.image = Image(source='roads/c.png', pos=(x_coord, y_coord), nocache=True)
            elif x == 'd':
                new_tile.image = Image(source='roads/d.png', pos=(x_coord, y_coord), nocache=True)
            elif x == 'e':
                new_tile.image = Image(source='roads/e.png', pos=(x_coord, y_coord), nocache=True)
            elif x == 'f':
                new_tile.image = Image(source='roads/f.png', pos=(x_coord, y_coord), nocache=True)
            elif x == 'g':
                new_tile.image = Image(source='roads/g.png', pos=(x_coord, y_coord), nocache=True)
            elif x == 'h':
                new_tile.image = Image(source='roads/h.png', pos=(x_coord, y_coord), nocache=True)
            elif x == 'i':
                new_tile.image = Image(source='roads/i.png', pos=(x_coord, y_coord), nocache=True)
            elif x == 'j':
                new_tile.image = Image(source='roads/j.png', pos=(x_coord, y_coord), nocache=True)
            elif x == 'k':
                new_tile.image = Image(source='roads/k.png', pos=(x_coord, y_coord), nocache=True)
            elif x == 'l':
                new_tile.image = Image(source='roads/l.png', pos=(x_coord, y_coord), nocache=True)
            elif x == 'm':
                new_tile.image = Image(source='roads/m.png', pos=(x_coord, y_coord), nocache=True)
            elif x == 'n':
                new_tile.image = Image(source='roads/n.png', pos=(x_coord, y_coord), nocache=True)
            elif x == 'o':
                new_tile.image = Image(source='roads/o.png', pos=(x_coord, y_coord), nocache=True)
            elif x == 'p':
                new_tile.image = Image(source='roads/p.png', pos=(x_coord, y_coord), nocache=True)
            elif x == 'q':
                new_tile.image = Image(source='roads/q.png', pos=(x_coord, y_coord), nocache=True)
            elif x == '0':
                new_tile.image = Image(source='grass.png', pos=(x_coord, y_coord), nocache=True)

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

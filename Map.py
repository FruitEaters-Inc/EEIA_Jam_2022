from kivy.uix.image import Image

import Tile
from business_logic import Dronex


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
    building_offset = 20

    for y in char_map:

        y_coord = y_counter * -40 + 451
        x_counter = 0

        for x in y:

            new_tile = Tile.Tile()
            new_tile.type = "road"

            x_coord = x_counter * 40 - 870

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
            elif x == 'r':
                new_tile.image = Image(source='roads/r.png', pos=(x_coord, y_coord), nocache=True)
            elif x == 's':
                new_tile.image = Image(source='roads/s.png', pos=(x_coord, y_coord), nocache=True)
            elif x == 't':
                new_tile.image = Image(source='roads/t.png', pos=(x_coord, y_coord), nocache=True)
                new_tile.is_permitted = False
                new_tile.can_give_interaction = False
                new_tile.type = "airport"
            elif x == 'u':
                new_tile.image = Image(source='roads/u.png', pos=(x_coord, y_coord), nocache=True)
                new_tile.is_permitted = False
                new_tile.can_give_interaction = False
                new_tile.type = "airport"
            elif x == 'v':
                new_tile.image = Image(source='roads/v.png', pos=(x_coord, y_coord), nocache=True)
                new_tile.is_permitted = False
                new_tile.can_give_interaction = False
                new_tile.type = "airport"
            elif x == 'w':
                new_tile.image = Image(source='roads/w.png', pos=(x_coord, y_coord), nocache=True)
                new_tile.is_permitted = False
                new_tile.can_give_interaction = False
                new_tile.type = "airport"
            elif x == 'x':
                new_tile.image = Image(source='roads/x.png', pos=(x_coord, y_coord), nocache=True)
                new_tile.is_permitted = False
                new_tile.can_give_interaction = False
                new_tile.type = "airport"
            elif x == 'y':
                new_tile.image = Image(source='roads/y.png', pos=(x_coord, y_coord), nocache=True)
                new_tile.is_permitted = False
                new_tile.can_give_interaction = False
                new_tile.type = "airport"
            elif x == '0':
                new_tile.image = Image(source='grass.png', pos=(x_coord, y_coord), nocache=True)
                new_tile.type = "grass"
            elif x == '1':
                new_tile = Dronex()
                new_tile.image = Image(source='dronex.png', pos=(x_coord, y_coord+building_offset), nocache=True)
                new_tile.type = "DRONEX"
                new_tile.can_give_interaction = False
            elif x == '#':
                new_tile.image = Image(source='roads/#.png', pos=(x_coord, y_coord), nocache=True)
                new_tile.can_give_interaction = False
                new_tile.type = "water"
            elif x == '[':
                new_tile.image = Image(source='roads/[.png', pos=(x_coord, y_coord), nocache=True)
                new_tile.can_give_interaction = False
                new_tile.type = "water"
            elif x == ']':
                new_tile.image = Image(source='roads/].png', pos=(x_coord, y_coord), nocache=True)
                new_tile.can_give_interaction = False
                new_tile.type = "water"
            elif x == '(':
                new_tile.image = Image(source='roads/(.png', pos=(x_coord, y_coord), nocache=True)
                new_tile.can_give_interaction = False
                new_tile.type = "water"
            elif x == ')':
                new_tile.image = Image(source='roads/).png', pos=(x_coord, y_coord), nocache=True)
                new_tile.can_give_interaction = False
                new_tile.type = "water"
            elif x == '-':
                new_tile.image = Image(source='roads/-.png', pos=(x_coord, y_coord), nocache=True)
                new_tile.can_give_interaction = False
                new_tile.type = "water"
            elif x == '_':
                new_tile.image = Image(source='roads/_.png', pos=(x_coord, y_coord), nocache=True)
                new_tile.can_give_interaction = False
                new_tile.type = "water"
            elif x == '{':
                new_tile.image = Image(source='roads/{.png', pos=(x_coord, y_coord), nocache=True)
                new_tile.can_give_interaction = False
                new_tile.type = "water"
            elif x == '}':
                new_tile.image = Image(source='roads/}.png', pos=(x_coord, y_coord), nocache=True)
                new_tile.can_give_interaction = False
                new_tile.type = "water"
            elif x == '^':
                new_tile.image = Image(source='roads/^.png', pos=(x_coord, y_coord), nocache=True)
                new_tile.can_give_interaction = False
                new_tile.type = "water"
            elif x == '%':
                new_tile.image = Image(source='roads/%.png', pos=(x_coord, y_coord), nocache=True)
                new_tile.can_give_interaction = False
                new_tile.type = "water"
            elif x == '&':
                new_tile.image = Image(source='roads/&.png', pos=(x_coord, y_coord), nocache=True)
                new_tile.can_give_interaction = False
                new_tile.type = "water"
            elif x == '=':
                new_tile.image = Image(source='roads/=.png', pos=(x_coord, y_coord), nocache=True)
                new_tile.can_give_interaction = False
                new_tile.type = "water"
            elif x == '+':
                new_tile.image = Image(source='roads/+.png', pos=(x_coord, y_coord), nocache=True)
                new_tile.can_give_interaction = False
                new_tile.type = "water"
            elif x == '$':
                new_tile.image = Image(source='roads/$.png', pos=(x_coord, y_coord), nocache=True)
                new_tile.can_give_interaction = False
                new_tile.type = "water"
            elif x == '@':
                new_tile.image = Image(source='roads/@.png', pos=(x_coord, y_coord), nocache=True)
                new_tile.can_give_interaction = False
                new_tile.type = "water"
            elif x == 'z':
                new_tile.image = Image(source='roads/z.png', pos=(x_coord, y_coord), nocache=True)
                new_tile.type = "building"
            elif x == 'A':
                new_tile.image = Image(source='buildings/A.png', pos=(x_coord, y_coord), nocache=True)
                new_tile.type = "building"
            elif x == 'B':
                new_tile.image = Image(source='buildings/B.png', pos=(x_coord, y_coord), nocache=True)
                new_tile.type = "building"
            elif x == 'C':
                new_tile.image = Image(source='buildings/C.png', pos=(x_coord, y_coord), nocache=True)
                new_tile.type = "building"
            elif x == 'D':
                new_tile.image = Image(source='buildings/D.png', pos=(x_coord, y_coord), nocache=True)
                new_tile.type = "building"
            elif x == 'E':
                new_tile.image = Image(source='buildings/E.png', pos=(x_coord, y_coord), nocache=True)
                new_tile.type = "building"
            elif x == 'F':
                new_tile.image = Image(source='buildings/F.png', pos=(x_coord, y_coord), nocache=True)
                new_tile.type = "building"
            elif x == 'G':
                new_tile.image = Image(source='buildings/G.png', pos=(x_coord, y_coord), nocache=True)
                new_tile.type = "building"
            elif x == 'H':
                new_tile.image = Image(source='buildings/H.png', pos=(x_coord, y_coord), nocache=True)
                new_tile.type = "building"
            elif x == 'I':
                new_tile.image = Image(source='buildings/I.png', pos=(x_coord, y_coord), nocache=True)
                new_tile.type = "building"
            elif x == 'J':
                new_tile.image = Image(source='buildings/J.png', pos=(x_coord, y_coord), nocache=True)
                new_tile.type = "building"
            elif x == 'K':
                new_tile.image = Image(source='buildings/K.png', pos=(x_coord, y_coord), nocache=True)
                new_tile.type = "building"
            elif x == 'L':
                new_tile.image = Image(source='buildings/L.png', pos=(x_coord, y_coord), nocache=True)
                new_tile.type = "building"
            elif x == 'M':
                new_tile.image = Image(source='buildings/M.png', pos=(x_coord, y_coord), nocache=True)
                new_tile.type = "building"
            elif x == 'N':
                new_tile.image = Image(source='buildings/N.png', pos=(x_coord, y_coord), nocache=True)
                new_tile.type = "building"
            elif x == 'O':
                new_tile.image = Image(source='buildings/O.png', pos=(x_coord, y_coord), nocache=True)
                new_tile.type = "building"
            elif x == 'P':
                new_tile.image = Image(source='buildings/P.png', pos=(x_coord, y_coord), nocache=True)
                new_tile.type = "building"
            elif x == 'R':
                new_tile.image = Image(source='buildings/R.png', pos=(x_coord, y_coord), nocache=True)
                new_tile.type = "building"
            elif x == 'S':
                new_tile.image = Image(source='buildings/S.png', pos=(x_coord, y_coord), nocache=True)
                new_tile.type = "building"
            elif x == 'T':
                new_tile.image = Image(source='buildings/T.png', pos=(x_coord, y_coord), nocache=True)
                new_tile.type = "building"
            elif x == 'U':
                new_tile.image = Image(source='buildings/U.png', pos=(x_coord, y_coord), nocache=True)
                new_tile.type = "building"
            elif x == 'V':
                new_tile.image = Image(source='buildings/V.png', pos=(x_coord, y_coord), nocache=True)
                new_tile.type = "building"
            elif x == 'X':
                new_tile.image = Image(source='buildings/X.png', pos=(x_coord, y_coord), nocache=True)
                new_tile.type = "grass"
            elif x == 'Y':
                new_tile.image = Image(source='buildings/Y.png', pos=(x_coord, y_coord), nocache=True)
                new_tile.type = "building"
            elif x == 'Z':
                new_tile.image = Image(source='buildings/Z.png', pos=(x_coord, y_coord), nocache=True)
                new_tile.type = "building"
            elif x == '2':
                new_tile.image = Image(source='buildings/2.png', pos=(x_coord, y_coord+building_offset), nocache=True)
                new_tile.type = "skyscraper"
                new_tile.is_permitted = False
                new_tile.can_give_interaction = False
            elif x == '3':
                new_tile.image = Image(source='buildings/3.png', pos=(x_coord, y_coord+building_offset), nocache=True)
                new_tile.type = "skyscraper"
                new_tile.is_permitted = False
                new_tile.can_give_interaction = False
            elif x == '4':
                new_tile.image = Image(source='buildings/4.png', pos=(x_coord, y_coord+building_offset), nocache=True)
                new_tile.type = "skyscraper"
                new_tile.is_permitted = False
                new_tile.can_give_interaction = False
            elif x == '5':
                new_tile.image = Image(source='buildings/5.png', pos=(x_coord, y_coord+building_offset), nocache=True)
                new_tile.type = "skyscraper"
                new_tile.is_permitted = False
                new_tile.can_give_interaction = False
            elif x == '6':
                new_tile.image = Image(source='buildings/6.png', pos=(x_coord, y_coord+building_offset), nocache=True)
                new_tile.type = "skyscraper"
                new_tile.is_permitted = False
                new_tile.can_give_interaction = False
            elif x == '7':
                new_tile.image = Image(source='buildings/7.png', pos=(x_coord, y_coord), nocache=True)
                new_tile.type = "base"
                new_tile.is_permitted = False
                new_tile.can_give_interaction = False
            elif x == '8':
                new_tile.image = Image(source='buildings/8.png', pos=(x_coord, y_coord), nocache=True)
                new_tile.type = "base"
                new_tile.is_permitted = False
                new_tile.can_give_interaction = False
            elif x == '9':
                new_tile.image = Image(source='buildings/9.png', pos=(x_coord, y_coord), nocache=True)
                new_tile.type = "base"
                new_tile.is_permitted = False
                new_tile.can_give_interaction = False
            elif x == '!':
                new_tile.image = Image(source='buildings/!.png', pos=(x_coord, y_coord), nocache=True)
                new_tile.type = "base"
                new_tile.is_permitted = False
                new_tile.can_give_interaction = False
            elif x == ';':
                new_tile.image = Image(source='buildings/;.png', pos=(x_coord, y_coord), nocache=True)
                new_tile.type = "base"
                new_tile.is_permitted = False
                new_tile.can_give_interaction = False
            elif x == '.':
                new_tile.image = Image(source='buildings/..png', pos=(x_coord, y_coord), nocache=True)
                new_tile.type = "grass"
            elif x == ',':
                new_tile.image = Image(source='buildings/,.png', pos=(x_coord, y_coord), nocache=True)
                new_tile.type = "grass"



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

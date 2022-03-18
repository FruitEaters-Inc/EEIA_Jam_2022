from kivy.uix.image import Image


def load_map(file):
    f = open(file)

    map_data = []

    for row in f.read().split('\n'):
        map_row = [c for c in row]
        map_data.append(map_row)

    f.close()
    return map_data


def map_isometrise(binary_map):
    iso_row = []
    iso_map = []
    y_counter = 0

    for y in binary_map:

        y_coord = y_counter * -20 + 520
        x_counter = 0

        for x in y:
            x_coord = x_counter * 40 - 940

            if x == '1':
                img = Image(source='road.png', pos=(x_coord, y_coord), nocache=True)
                iso_row.append(img)
            elif x == '0':
                img = Image(source='grass.png', pos=(x_coord, y_coord), nocache=True)
                iso_row.append(img)

            x_counter += 1

        y_counter += 1

        iso_map.append(iso_row.copy())
        iso_row.clear()
        y_counter += 1

    return iso_map


def build_map(iso_map, layout):
    for y in iso_map:
        for x in y:
            if x is not None:
                layout.add_widget(x)

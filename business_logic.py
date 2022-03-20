import random
from Tile import Tile


class Finance:
    def __init__(self) -> None:
        self.budget = 0


class Dronex(Tile):
    def __init__(self) -> None:
        super().__init__()


busy_tiles = []


def remove_tile(tile):
    global busy_tiles
    for t in busy_tiles:
        if t == tile:
            print(busy_tiles.pop(busy_tiles.index(t)))


thief = False


def get_thief():
    global thief
    return thief


def reset_thief():
    global thief
    thief = False


RANDOM_PROB = 0.05


class EventSpawner:
    def __init__(self, tile_map) -> None:
        self.tileMap = tile_map
        self.eventList = []

    def spawn_event(self):
        global thief
        if random.random() < RANDOM_PROB:
            thief = True
            return

        global busy_tiles
        eventable = False
        while not eventable:
            tile = random.choice(random.choice(self.tileMap))
            if tile.can_give_interaction:
                if tile not in busy_tiles:
                    eventable = True
                    self.eventList.append(tile.get_interaction())
                    busy_tiles.append(tile)


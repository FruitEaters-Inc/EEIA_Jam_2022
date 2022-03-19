import random
from Tile import Tile



class Finance:
    def __init__(self) -> None:
        self.budget = 0


class Dronex(Tile):
    def __init__(self) -> None:
        super().__init__()


class EventSpawner:
    def __init__(self, tile_map) -> None:
        self.tileMap = tile_map
        self.eventList = []

    def spawn_event(self) -> None:
        eventable = False
        while not eventable:
            tile = random.choice(random.choice(self.tileMap))
            if tile.can_give_interaction:
                eventable = True
                self.eventList.append(tile.get_interaction())


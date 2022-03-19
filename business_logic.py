import random

class Finance:
    def __init__(self) -> None:
        self.budget = 0


class DronPolSa:
    def __init__(self) -> None:
        pass

class EventSpawner:
    def __init__(self, tileMap) -> None:
        self.tileMap = tileMap
        self.eventList = []

    def spawnEvent(self) -> None:
        self.eventList.append(random.choice(random.choice(self.tileMap)).get_interaction())
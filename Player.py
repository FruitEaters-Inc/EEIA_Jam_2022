import Drone
from Tile import Tile


class Player:
    def __init__(self, HQ_tile: Tile):
        self.HQ_tile = HQ_tile
        self.wealth = 500
        self.drone_count = 0
        self.drones = []

    def increaseWealth(self, count: int) -> None:
        self.wealth += count

    def reduceWealth(self, count: int) -> None:
        self.wealth -= count

    def addDrone(self) -> None:
        self.drones.append(Drone.Drone(self.HQ_tile, 10))
        self.drone_count += 1

    def removeDrone(self) -> None:
        self.drones.pop()
        self.drone_count -= 1

    def purchaseDrone(self) -> None:
        self.reduceWealth(250)
        self.addDrone()

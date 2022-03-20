import Drone
from Tile import Tile

DRONE_PRICE = 250


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

    def canAffordDrone(self) -> bool:
        return self.wealth >= DRONE_PRICE

    def purchaseDrone(self) -> None:
        if self.canAffordDrone():
            self.reduceWealth(DRONE_PRICE)
            self.addDrone()

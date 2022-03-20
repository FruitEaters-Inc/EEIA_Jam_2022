import Drone
from Tile import Tile

STARTING_WEALTH = 500
DRONE_BUY_PRICE = 250
DRONE_SELL_PRICE = 100


class Player:
    def __init__(self, HQ_tile: Tile):
        self.HQ_tile = HQ_tile
        self.wealth = STARTING_WEALTH
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
        return self.wealth >= DRONE_BUY_PRICE

    def sellDrone(self) -> None:
        self.increaseWealth(DRONE_SELL_PRICE)

    def purchaseDrone(self) -> None:
        if self.canAffordDrone():
            self.reduceWealth(DRONE_BUY_PRICE)
            self.addDrone()

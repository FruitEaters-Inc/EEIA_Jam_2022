class Player:
    def __init__(self):
        self.wealth = 500
        self.drone_count = 0

    def increaseWealth(self, count: int) -> None:
        self.wealth += count

    def reduceWealth(self, count: int) -> None:
        self.wealth -= count

    def addDrone(self) -> None:
        self.drone_count += 1

    def removeDrone(self) -> None:
        self.drone_count -= 1

    def purchaseDrone(self) -> None:
        self.reduceWealth(500)
        self.addDrone()

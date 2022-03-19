import Drone
import Map
from kivy.core.window import Window
from kivy.uix.relativelayout import RelativeLayout
from kivy.app import App
import kivy

import Tile

kivy.require('2.0.0')
Window.size = (1920, 1080)
Window.clearcolor = (78 / 255, 173 / 255, 245 / 255, 1)


# Window.fullscreen = True


class MyApp(App):
    def __init__(self):
        super().__init__()

        self.my_drones = None
        self.map = None
        self.tile_map = None

        self.layout = None

    def build(self):
        self.map = Map.load_map("map.txt")
        self.tile_map = Map.map_organise(self.map)

        self.layout = RelativeLayout()

        Map.build_map(self.tile_map, self.layout)

        Tile.find_neighbours(self.tile_map)

        drone_spawn = Tile.find_tile(self.tile_map, "DRONEX")
        drone_spawn = drone_spawn.neighbours["up"]

        new_drone = Drone.Drone(drone_spawn, 10)

        self.my_drones = []
        self.my_drones.append(new_drone)

        for drone in self.my_drones:
            drone.draw_drone(self.layout)

        return self.layout


MyApp().run()

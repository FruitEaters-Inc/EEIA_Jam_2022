import Drone
import Map
from kivy.core.window import Window
from kivy.uix.relativelayout import RelativeLayout
from kivy.app import App
from kivy.clock import Clock
import kivy

import Tile
import business_logic

kivy.require('2.0.0')
Window.size = (1920, 1080)
Window.clearcolor = (78 / 255, 173 / 255, 245 / 255, 1)


# Window.fullscreen = True


class MyApp(App):
    def __init__(self):
        super().__init__()

        self.drone_layout = None
        self.event = None
        self.my_drones = None
        self.map = None
        self.tile_map = None

        self.layout = None

    def build(self):
        self.map = Map.load_map("map.txt")
        self.tile_map = Map.map_organise(self.map)

        self.layout = RelativeLayout()
        self.drone_layout = RelativeLayout()

        Map.build_map(self.tile_map, self.layout)

        Tile.find_neighbours(self.tile_map)

        drone_spawn = Tile.find_tile(self.tile_map, "DRONEX")
        drone_spawn = drone_spawn.neighbours["up"]

        new_drone = Drone.Drone(drone_spawn, 10)

        self.my_drones = []
        self.my_drones.append(new_drone)

        for drone in self.my_drones:
            drone.draw_drone(self.drone_layout)
            drone.move_direction("left")
            drone.draw_drone(self.drone_layout)

        self.layout.add_widget(self.drone_layout)

        my_events = business_logic.EventSpawner(self.tile_map)

        self.event = Clock.schedule_interval(lambda instance: my_events.spawn_event(), 10)

        return self.layout


MyApp().run()

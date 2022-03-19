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
        self.main_loop = None
        self.event_clock = None

        self.my_events = None
        self.my_drones = None

        self.main_layout = None
        self.event_layout = None
        self.drone_layout = None

        self.map = None
        self.tile_map = None

    def build(self):
        self.map = Map.load_map("map.txt")
        self.tile_map = Map.map_organise(self.map)

        self.main_layout = RelativeLayout()
        self.drone_layout = RelativeLayout()
        self.event_layout = RelativeLayout()

        Map.build_map(self.tile_map, self.main_layout)

        Tile.find_neighbours(self.tile_map)

        drone_spawn = Tile.find_tile(self.tile_map, "DRONEX")
        drone_spawn = drone_spawn.neighbours["up"]

        new_drone = Drone.Drone(drone_spawn, 10)

        self.my_drones = []
        self.my_drones.append(new_drone)

        self.main_layout.add_widget(self.drone_layout)

        self.my_events = business_logic.EventSpawner(self.tile_map)

        self.main_loop = Clock.schedule_interval(lambda instance: self.refresh(), 1)

        self.event_clock = Clock.schedule_interval(lambda instance: self.my_events.spawn_event(), 10)

        self.refresh()

        return self.main_layout

    def refresh(self):
        self.drone_layout.clear_widgets()

        for drone in self.my_drones:
            drone.draw_drone(self.drone_layout)

        self.event_layout.clear_widgets()
        for event in self.my_events.eventList:
            event.draw_event(self.event_layout)


MyApp().run()

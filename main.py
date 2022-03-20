from kivy.uix.button import Button
from kivy.uix.label import Label

import Map
from kivy.core.window import Window
from kivy.uix.relativelayout import RelativeLayout
from kivy.app import App
from kivy.clock import Clock
from kivy.uix.image import Image
from kivy.config import Config
import kivy

import Player
import Tile
import Event
import business_logic

kivy.require('2.0.0')
Window.size = (1920, 1080)
Window.clearcolor = (78 / 255, 173 / 255, 245 / 255, 1)

Window.fullscreen = True

Config.set('graphics', 'width', '1920')
Config.set('graphics', 'height', '1080')

Config.set('graphics', 'window_state', 'maximized')
Config.set('graphics', 'resizable', False)


class MyApp(App):
    def __init__(self):
        super().__init__()

        self.clicker_display = None
        self.clicker_buy_button = None
        self.counter_button = None
        self.drone_buy_button = None
        self.main_loop = None
        self.event_clock = None
        self.autoclicker_clock = None
        self.drone_movement = None

        self.my_events = None
        self.player = None

        self.main_layout = None
        self.event_layout = None
        self.drone_layout = None
        self.map_layout = None

        self.wealth_display = None
        self.drone_display = None

        self.map = None
        self.tile_map = None

    def build(self):
        self.map = Map.load_map("map.txt")
        self.tile_map = Map.map_organise(self.map)

        self.main_layout = RelativeLayout()
        self.drone_layout = RelativeLayout()
        self.event_layout = RelativeLayout()
        self.map_layout = RelativeLayout()

        desk = Image(source='desk.png', pos=(-130, -471), allow_stretch=False,
                     nocache=True)
        self.map_layout.add_widget(desk)

        Map.build_map(self.tile_map, self.map_layout)

        Tile.find_neighbours(self.tile_map)

        drone_spawn = Tile.find_tile(self.tile_map, "DRONEX")
        drone_spawn = drone_spawn.neighbours["up"]

        self.player = Player.Player(drone_spawn)

        screen = Image(source='screen.png', pos=(-130, 14), allow_stretch=False,
                       nocache=True)
        self.map_layout.add_widget(screen)

        self.clicker_buy_button = Button(background_normal='autoclicker.png', background_down='autoclicker_down.png',
                                        pos=(1010, 10), size_hint=(None, None), size=(262, 172))
        self.clicker_buy_button.bind(on_press=lambda instance: self.IncreaseAutoclicker())
        self.map_layout.add_widget(self.clicker_buy_button)

        self.drone_buy_button = Button(background_normal='drone_buy.png', background_down='drone_buy_down.png', pos=(1245, 10),
                                       size_hint=(None, None), size=(262, 172))
        self.drone_buy_button.bind(on_press=lambda instance: self.player.purchaseDrone())
        self.map_layout.add_widget(self.drone_buy_button)

        self.counter_button = Button(background_normal='counter.png', background_down='counter.png', pos=(200, 10),
                                     size_hint=(None, None), size=(532, 130))
        self.map_layout.add_widget(self.counter_button)

        self.wealth_display = Label(text=str(self.player.wealth),
                                    pos=(-510, -457), font_size=40, )
        self.map_layout.add_widget(self.wealth_display)

        self.drone_display = Label(text=str(self.player.drone_count),
                                   pos=(-150, -457), font_size=40)
        self.map_layout.add_widget(self.drone_display)

        self.clicker_display = Label(text=str(self.player.autoclicker),
                                     pos=(-150, -457), font_size=40)
        self.map_layout.add_widget(self.clicker_display)

        lama = Image(source='lama_basista.png', pos=(830, 300),
                     allow_stretch=False, nocache=True)

        lama2 = Image(source='lama_chlopak.png', pos=(830, 50),
                      allow_stretch=False, nocache=True)

        lama3 = Image(source='lama_zaklin.png', pos=(830, -200),
                      allow_stretch=False, nocache=True)
        self.map_layout.add_widget(lama)
        self.map_layout.add_widget(lama2)
        self.map_layout.add_widget(lama3)

        self.my_events = business_logic.EventSpawner(self.tile_map)

        self.main_loop = Clock.schedule_interval(
            lambda instance: self.refresh(), 0.5)

        self.event_clock = Clock.schedule_interval(
            lambda instance: self.my_events.spawn_event(), 4)

        self.drone_movement = Clock.schedule_interval(
            lambda instance: self.move_drones(), 1)

        self.refresh()

        return self.main_layout

    def IncreaseAutoclicker(self):
        if self.player.purchaseAutoclicker():
            if self.autoclicker_clock is not None:
                self.autoclicker_clock.cancel()
            self.autoclicker_clock = Clock.schedule_interval(
                lambda instance: self.autoclick(), 10 / self.player.autoclicker)

    def autoclick(self):
        filtered = list(filter(lambda x: not x.is_added_to_destinations, self.my_events.eventList))
        if len(filtered) != 0:
            Event.add_destination(filtered[0])

    def refresh(self):
        self.main_layout.clear_widgets()
        self.main_layout.add_widget(self.map_layout)
        self.drone_layout.clear_widgets()

        self.wealth_display.text = str(self.player.wealth)
        self.drone_display.text = str(self.player.drone_count)

        for drone in self.player.drones:
            if drone is not None:
                if len(drone.movePath) != 0:
                    drone.draw_drone(self.drone_layout)

        self.main_layout.add_widget(self.drone_layout)

        self.event_layout.clear_widgets()
        for event in self.my_events.eventList:
            if event is not None:
                event.draw_event(self.event_layout)

        self.main_layout.add_widget(self.event_layout)

        return self.main_layout

    def move_drones(self):
        for event in self.my_events.eventList:
            if event.obsolete:
                self.my_events.eventList.pop(self.my_events.eventList.index(event))
                self.player.increaseWealth(50)

        for drone in self.player.drones:
            if len(drone.movePath) == 0 and len(Event.destinations) != 0:
                event = Event.destinations.pop()
                drone.add_target(event)
                drone.create_path(event.tile, event.target)
                event.image.source = "green_alert.zip"
                event.image.reload()
                event.remove_button()

        for drone in self.player.drones:
            drone.move_to(drone.pop_move())


MyApp().run()
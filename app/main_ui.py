
from kivy.properties import BooleanProperty
from kivy.uix.screenmanager import ScreenManager
from kivymd.uix.screen import MDScreen
from kivymd.uix.gridlayout import MDGridLayout
from kivymd.uix.carousel import MDCarousel
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.label import MDLabel

class Manager(ScreenManager):
    def switch_to_home_screen(self):
        self.current='home screen'
        self.transition.direction='right'

class HomeScreen(MDScreen):
    pass

class CreateTask(MDScreen):
    pass
class Task(MDGridLayout):
    cols=2

class TaskSlider(MDCarousel):
    loop=BooleanProperty(True)
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        for i in range(10):
            text=MDLabel(text=f'Task at slide {i}',halign='center',adaptive_height=True)
            box=MDBoxLayout(orientation='vertical')
            box.add_widget(text)
            self.add_widget(box)



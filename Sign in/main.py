import kivy
kivy.require('1.1.1')

from kivy.app import App # import App
from kivy.uix.widget import Widget
from kivy.properties import NumericProperty, ReferenceListProperty,\
    ObjectProperty
from kivy.vector import Vector
from kivy.clock import Clock
from kivy.uix.button import Button
from kivy.uix.slider import Slider
from kivy.uix.gridlayout import GridLayout


# Python Package


class MainOcean(Widget):
    pass
    

class OceanApp(App):
    def build(self):
        MainScreen=MainOcean()
        return MainScreen


if __name__ == '__main__':
    OceanApp().run()

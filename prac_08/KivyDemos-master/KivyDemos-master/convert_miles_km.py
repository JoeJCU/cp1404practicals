"""
CP1404 Practical 8
Kivy GUI program
Started 18/11/2024
"""

from kivy.app import App
from kivy.lang import Builder
from kivy.core.window import Window

class ConvertMilesKm(App):
    """ GUI to convert Miles to Km """

    def build(self):
        """ build the Kivy app """
        Window.size = (200, 100) #(x,y)
        self.title = "Miles to Km"
        self.root = Builder.load_file('convert_miles_km.kv')
        return self.root


    def convertion(self):

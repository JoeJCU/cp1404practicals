"""
CP1404 Practical 8
Kivy GUI program
Started 18/11/2024
"""

from kivy.app import App
from kivy.lang import Builder
from kivy.core.window import Window

conversionRate = 1.60934

class ConvertMilesKm(App):
    """ GUI to convert Miles to Km """

    def build(self):
        """ build the Kivy app """
        # Window.size = (200, 100) #(x,y)
        self.title = "Miles to Km"
        self.root = Builder.load_file('convert_miles_km.kv')
        return self.root

    def handle_convertion(self, text):
        try:
            miles = float(text)
            km = miles * conversionRate
            self.root.ids.output_distance.text = str(km)
        except ValueError:
            miles = 0

    def handle_incrementation(self, text, value):
        try:
            miles = int(text)
        except ValueError:
            miles = 0

        miles += value # 1 or -1 increments
        self.root.ids.input_number.text = str(miles) #change the value in the text field


        


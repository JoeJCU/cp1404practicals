"""
CP 1404 Practical 4, Joe David Mathew, silver service taxi
"""
from taxi import Taxi

class Silverservicetaxi(Taxi):
    def __init__(self, name, fuel, fanciness):
        super().__init__(name, fuel)
        self.fanciness = fanciness
        self.flagfall = 4.50
        self.price_per_km *= fanciness

    def get_fare(self):
        return super().get_fare() + self.flagfall  #total fare including the flagfall

    def __str__(self):
        return f"{super().__str__()} Flagfall: ${self.flagfall}"

    def start_fare(self):
        """Begin a new fare."""
        self.current_fare_distance = 0
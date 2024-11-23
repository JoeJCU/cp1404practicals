"""
CP 1404 Practical 4, Joe David Mathew, unreliable Car
"""

import random
from prac_09.car import Car

class Unreliablecar(Car):

    def __init__(self, name, fuel, reliability):
        super().__init__(name, fuel)
        self.reliability = reliability  #stand alone attribute


    def drive(self, distance):
        rand_num = random.randint(0,100)

        if rand_num < self.reliability:
            return super().drive(distance) #does the function
        else:
            return 0

    def __str__(self):
        return f"car: name={self.name}, fuel={self.fuel}, reliability={self.reliability}"

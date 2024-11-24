
"""
CP 1404 Practical 4, Joe David Mathew, Band
"""

class Band:
    """Class for band objects"""
    def __init__(self, name=""):
        self.name = name
        self.musicians = []

    def add(self, musician):
        self.musicians.append(musician)



    def play(self):

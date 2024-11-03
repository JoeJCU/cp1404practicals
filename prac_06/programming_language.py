
class programmingLanguage:
    def __init__(self, name= "", typed= "", reflect= False, year= 0):
        self.name = name
        self.typed = typed
        self.reflect = reflect
        self.year = year
        print(self)

    def __str__(self):
        return (f"{self.name}, Typing= {self.typed}, Reflection= {self.reflect}, Year= {self.year}")


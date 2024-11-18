
class guitar_class:
    def __init__(self, name= "", year= 0, cost= 0):
        self.name = name
        self.year = year
        self.cost = cost

        print(self)

    def __str__(self):
        return f"{self.name} ({self.year}) : ${self.cost:.2f}"

    def __lt__(self, other):  #sorting(less than)
        return self.year < other.year






    def get_age(self):
        current_year = 2024  # You could also use datetime.datetime.now().year for dynamic year
        return current_year - self.year

    def is_vintage(self):
            return self.get_age() >= 50 #should return true
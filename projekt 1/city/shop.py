from city.basic_location import BasicLocation

class Shop(BasicLocation):
    def __init__(self):
        super().__init__("General Store", "A store that sells a variety of items you might need on your adventures.")

    def enter(self):
        super().enter()
        print("Browse our goods and make your purchases.")

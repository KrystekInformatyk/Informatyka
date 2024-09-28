from city.basic_location import BasicLocation

class Hotel(BasicLocation):
    def __init__(self):
        super().__init__("Grand Hotel", "A luxurious place to stay with comfortable beds and excellent service.")

    def enter(self):
        super().enter()
        print("Enjoy our five-star service and amenities.")

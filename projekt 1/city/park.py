from city.basic_location import BasicLocation

class Park(BasicLocation):
    def __init__(self):
        super().__init__("Greenway Park", "A peaceful park with green trees and a calming atmosphere.")

    def enter(self):
        super().enter()
        print("Take a deep breath and enjoy the nature around you.")

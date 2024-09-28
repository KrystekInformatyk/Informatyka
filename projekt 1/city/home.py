from city.basic_location import BasicLocation

class Home(BasicLocation):
    def __init__(self):
        super().__init__("Your Home", "This is where you live. It's a cozy little place just for you.")

    def enter(self):
        super().enter()
        print("Feel at home. Rest and recover.")

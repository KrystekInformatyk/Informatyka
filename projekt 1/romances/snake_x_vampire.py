from romances.basic_romances import BasicRomances

class SnakeXVampire(BasicRomances):
    def __init__(self):
        super().__init__(["Snake", "Vampire"])

    def detail_romance(self):
        print("The dark allure between the Snake and the Vampire captivates both.")

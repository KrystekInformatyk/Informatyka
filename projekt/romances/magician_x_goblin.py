from romances.basic_romances import BasicRomances

class MagicianXGoblin(BasicRomances):
    def __init__(self):
        super().__init__(["Magician", "Goblin"])

    def detail_romance(self):
        print("An unexpected romance blossoms between the Magician and the Goblin, full of surprises.")

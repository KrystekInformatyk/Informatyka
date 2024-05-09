from romances.basic_romances import BasicRomances

class VampireXMagician(BasicRomances):
    def __init__(self):
        super().__init__(["Vampire", "Magician"])

    def detail_romance(self):
        print("A mystical and enchanting romance unfolds between the Vampire and the Magician.")

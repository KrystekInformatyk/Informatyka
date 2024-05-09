from romances.basic_romances import BasicRomances

class GoblinXSnake(BasicRomances):
    def __init__(self):
        super().__init__(["Goblin", "Snake"])

    def detail_romance(self):
        print("The Goblin and the Snake find an unlikely but touching bond.")

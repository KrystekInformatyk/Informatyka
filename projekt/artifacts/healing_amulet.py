from artifacts.basic_artifacts import BasicArtifact

class HealingAmulet(BasicArtifact):
    def __init__(self):
        super().__init__("Healing Amulet", "Restores a large amount of health over time.", 30)

    def activate(self, character):
        if hasattr(character, 'hp'):
            character.hp += self.power
            print(f"{self.name} activated by {character.name}. Restores {self.power} health points.")
        else:
            print(f"{self.name} cannot be used by {character.name} as they lack 'hp' attribute.")

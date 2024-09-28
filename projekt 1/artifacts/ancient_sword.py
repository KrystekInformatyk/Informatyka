from artifacts.basic_artifacts import BasicArtifact

class AncientSword(BasicArtifact):
    def __init__(self):
        super().__init__("Ancient Sword", "Increases attack power significantly.", 50)

    def activate(self, character):
        if hasattr(character, 'attack_power'): 
            character.attack_power += self.power
            print(f"{self.name} equipped by {character._name}. Attack power increased by {self.power}.")
        else:
            print(f"{self.name} cannot be used by {character._name} as they lack 'attack_power' attribute.")


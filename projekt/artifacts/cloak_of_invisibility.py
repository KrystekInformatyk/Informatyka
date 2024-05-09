from artifacts.basic_artifacts import BasicArtifact

class CloakOfInvisibility(BasicArtifact):
    def __init__(self):
        super().__init__("Cloak of Invisibility", "Grants temporary invisibility.", 0)

    def activate(self, character):
        print(f"{self.name} activated by {character.name}. {character.name} is now invisible.")

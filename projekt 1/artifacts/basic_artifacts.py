class BasicArtifact:
    def __init__(self, name, description, power):
        self.name = name
        self.description = description
        self.power = power

    def activate(self, character):
        """ Activate the artifact's effect on the character. """
        print(f"{self.name} activated by {character.name}. {self.description}")

    def __str__(self):
        return f"{self.name} ({self.description}, Power: {self.power})"

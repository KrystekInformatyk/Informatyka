class BasicLocation:
    def __init__(self, name, description):
        self.name = name
        self.description = description

    def enter(self):
        print(f"You have entered {self.name}. {self.description}")

    def explore(self):
        print(f"Exploring {self.name}...")

    def leave(self):
        print(f"You are leaving {self.name}.")

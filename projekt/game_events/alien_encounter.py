from game_events.basic_events import BasicEvents

class AlienEncounter(BasicEvents):
    def __init__(self):
        super().__init__()
        self.description = "Encounter with aliens with different options."
        self.options = ["Negotiate peace", "Fight", "Flee"]

    def encounter(self):
        super().start_event()
        print("You have encountered aliens! What do you do?")
        for index, option in enumerate(self.options, start=1):
            print(f"{index} - {option}")
        choice = int(input("Enter your choice (number): "))
        if 1 <= choice <= len(self.options):
            print(f"You chose to {self.options[choice-1]}!")
        else:
            print("Invalid choice, returning to main menu.")

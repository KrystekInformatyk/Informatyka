from game_events.basic_events import BasicEvents

class TreasureHunt(BasicEvents):
    def __init__(self):
        super().__init__()
        self.description = "Hunt for treasures in various locations."
        self.locations = ["Ancient Castle", "Sunken Ship", "Forgotten Desert"]

    def start_hunt(self):
        super().start_event()
        print("Where do you want to hunt for treasure?")
        for index, location in enumerate(self.locations, start=1):
            print(f"{index} - {location}")
        choice = int(input("Enter your choice (number): "))
        if 1 <= choice <= len(self.locations):
            print(f"You are now hunting for treasure in the {self.locations[choice-1]}!")
        else:
            print("Invalid choice, returning to main menu.")

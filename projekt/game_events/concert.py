from game_events.basic_events import BasicEvents

class Concert(BasicEvents):
    def __init__(self):
        super().__init__()
        self.description = "Concert of various artists."
        self.artists = ["Travis Scott", "Lady Gaga", "Billie Eilish"]

    def attend_concert(self):
        super().start_event()
        print("Which concert do you want to attend?")
        for index, artist in enumerate(self.artists, start=1):
            print(f"{index} - {artist}")
        choice = int(input("Enter your choice (number): "))
        if 1 <= choice <= len(self.artists):
            print(f"You are now attending the concert of {self.artists[choice-1]}!")
        else:
            print("Invalid choice, returning to main menu.")

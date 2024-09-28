from game_events.basic_events import BasicEvents

class TimeMachine(BasicEvents):
    def __init__(self):
        super().__init__()
        self.description = "Travel through different years."
        self.years = [2015, 1905, 966]

    def travel_through_time(self):
        super().start_event()
        print("To which year do you want to travel?")
        for index, year in enumerate(self.years, start=1):
            print(f"{index} - {year}")
        choice = int(input("Enter your choice (number): "))
        if 1 <= choice <= len(self.years):
            print(f"You have traveled to the year {self.years[choice-1]}!")
        else:
            print("Invalid choice, returning to main menu.")

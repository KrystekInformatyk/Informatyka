from characters.mage import Mage
from characters.goblin import Goblin
from characters.vampire import Vampire
from characters.snake import Snake
from city.hotel import Hotel
from city.shop import Shop
from city.home import Home
from city.park import Park
from game_events.concert import Concert
from game_events.time_machine import TimeMachine
from game_events.treasure_hunt import TreasureHunt
from game_events.alien_encounter import AlienEncounter
from romances.goblin_x_snake import GoblinXSnake
from romances.magician_x_goblin import MagicianXGoblin
from romances.snake_x_vampire import SnakeXVampire
from romances.vampire_x_magician import VampireXMagician
from artifacts.ancient_sword import AncientSword
from artifacts.healing_amulet import HealingAmulet
import os
import sys

def one_on_one_fight(hero):
    opponent = Goblin()
    opponent.regenerate()
    hero.regenerate()
    while hero.is_alive() and opponent.is_alive():
        hero.reduce_hp(opponent.fight())
        opponent.reduce_hp(hero.fight())
    if not hero.is_alive():
        print("You gave your all today !!!")
    hero.add_gold(opponent.drop())

def visit_location():
    locations = {
        '1': Hotel(),
        '2': Shop(),
        '3': Home(),
        '4': Park()
    }

    print("Choose a location to visit:")
    print("1 - Hotel: A luxurious place to stay.")
    print("2 - Shop: Buy or sell goods.")
    print("3 - Home: Rest and recover.")
    print("4 - Park: Relax and enjoy nature.")

    choice = input("Enter your choice (1-4): ")

    if choice in locations:
        locations[choice].enter()
    else:
        print("Invalid choice. Returning to main menu.")

def start_a_romance():
    romances = {
        '1': GoblinXSnake(),
        '2': MagicianXGoblin(),
        '3': SnakeXVampire(),
        '4': VampireXMagician()
    }

    print("Choose a romance to start:")
    print("1 - Goblin x Snake")
    print("2 - Magician x Goblin")
    print("3 - Snake x Vampire")
    print("4 - Vampire x Magician")

    choice = input("Enter your choice (1-4): ")

    if choice in romances:
        romances[choice].start_romance()
    else:
        print("Invalid choice. Returning to main menu.")

def participate_in_event():
    events = {
        '1': Concert(),
        '2': TimeMachine(),
        '3': TreasureHunt(),
        '4': AlienEncounter()
    }

    print("Choose an event to participate in:")
    print("1 - Concert: Enjoy a live performance.")
    print("2 - Time Machine: Travel through time.")
    print("3 - Treasure Hunt: Search for hidden treasures.")
    print("4 - Alien Encounter: Face an unexpected alien visit.")

    choice = input("Enter your choice (1-4): ")

    if choice in events:
        if choice == '1':
            events[choice].attend_concert()
        elif choice == '2':
            events[choice].travel_through_time()
        elif choice == '3':
            events[choice].start_hunt()
        elif choice == '4':
            events[choice].encounter()
    else:
        print("Invalid choice. Returning to main menu.")

def manage_artifacts(character):
    artifacts = {
        '1': AncientSword(),
        '2': HealingAmulet()
    }

    print("Available Artifacts:")
    print("1 - Ancient Sword: A powerful sword that increases your attack.")
    print("2 - Healing Amulet: An amulet that gradually restores health.")

    choice = input("Choose an artifact to use (1-2): ")

    if choice in artifacts:
        artifacts[choice].activate(character)
    else:
        print("Invalid choice. Returning to main menu.")

def clear_screen():
    print("\n" * 100)

def main_game():
    print("Select a Character Class")
    print("a - Mage")
    print("b - Vampire")
    print("c - Snake")
    print("d - Goblin")

    choice = input().lower()
    if choice == 'a':
        my_hero = Mage()
    elif choice == 'b':
        my_hero = Vampire()
    elif choice == 'c':
        my_hero = Snake()
    elif choice == 'd':
        my_hero = Goblin()
    else:
        print("Invalid choice, defaulting to Mage.")
        my_hero = Mage()

    while my_hero.is_alive():
        clear_screen()
        print("\nMain Menu")
        print("a - Adventure")
        print("v - Visit a location")
        print("p - Participate in an event")
        print("r - Rest")
        print("e - Exit")
        print("s - Start a romance")
        print("m - Manage Artifacts")

        choice = input("Choose an option: ").lower()

        if choice == 'a':
            one_on_one_fight(my_hero)
        elif choice == 'v':
            visit_location()
        elif choice == 'p':
            participate_in_event()
        elif choice == 's':
            start_a_romance()
        elif choice == 'm':
            manage_artifacts(my_hero)
        elif choice == 'r':
            my_hero.total_rest()
        elif choice == 'e':
            print("Thank you for playing!")
            sys.exit()
        else:
            print("Invalid choice. Please choose again.")

if __name__ == '__main__':
    main_game()

print("Thank you for playing !!!")

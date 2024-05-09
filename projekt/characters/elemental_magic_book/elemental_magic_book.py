from random import randint

class ElementalSpellBook:  # Poprawiona literówka w nazwie klasy

    def __init__(self) -> None:
        self._unlocked_fire_ball = True
        self._unlocked_lightning = False  # Poprawiona literówka w nazwie atrybutu
        self._unlocked_elemental_annihilation = False

    def fire_ball(self, character):
        if character._mana >= 20:
            character._mana -= 20
            return 200
        else:
            print("There wasn't enough mana to complete the spell")
            return 0
        
    def lightning(self, character):  # Poprawiona literówka w nazwie metody
        if character._mana >= 100:
            character._mana -= 100
            return randint(1, 1000)
        else:
            print("There wasn't enough mana to complete the spell")
            return 0
        
    def elemental_annihilation(self, character):  # Poprawiona literówka w nazwie metody i zmiennej
        attack = 0
        for i in range(character._mana):
            attack = i * 4
        character._mana = 0
        return attack
    
    def choose_spell(self, character):
        while True:
            try:
                print(f"a \t Fire Ball available? {self._unlocked_fire_ball}")
                print(f"b \t Lightning available? {self._unlocked_lightning}")
                print(f"c \t Elemental Annihilation available? {self._unlocked_elemental_annihilation}")
                print(f"e \t Close the book")
                inp = input().lower()
                if inp == "a" and self._unlocked_fire_ball:
                    return self.fire_ball(character)
                elif inp == "b" and self._unlocked_lightning:
                    return self.lightning(character)
                elif inp == "c" and self._unlocked_elemental_annihilation:
                    return self.elemental_annihilation(character)
                elif inp == "e":
                    print("Closing the book")
                    break
                else:
                    print("This spell has not been unlocked yet or does not exist.")
            except Exception as e:
                print(f"An error occurred: {e}")

    def unlock_spells(self, character):  # Poprawiona literówka w nazwie metody
        while True:
            try:
                print(f"a -1000\t Fire Ball available? {self._unlocked_fire_ball}")
                print(f"b -5000g \t Lightning available? {self._unlocked_lightning}")
                print(f"c -10000g \t Elemental Annihilation available? {self._unlocked_elemental_annihilation}")
                print(f"e \t Close the book")
                inp = input().lower()
                if inp == "a" and not self._unlocked_fire_ball and character._gold >= 1000:
                    self._unlocked_fire_ball = True
                    print("Fire Ball unlocked!")
                elif inp == "b" and not self._unlocked_lightning and character._gold >= 5000:
                    self._unlocked_lightning = True
                    print("Lightning unlocked!")
                elif inp == "c" and not self._unlocked_elemental_annihilation and character._gold >= 10000:
                    self._unlocked_elemental_annihilation = True
                    print("Elemental Annihilation unlocked!")
                elif inp == "e":
                    print("Closing the book")
                    break
                else:
                    if inp in ["a", "b", "c"]:
                        print("Not enough gold or you already know this spell.")
                    else:
                        print("This option does not exist.")
            except Exception as e:
                print(f"An error occurred: {e}")

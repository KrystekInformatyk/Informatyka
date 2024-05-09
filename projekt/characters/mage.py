from characters.basic_character import BasicCharacter
from characters.elemental_magic_book.elemental_magic_book import ElementalSpellBook

class Mage(BasicCharacter):
    def __init__(self):
        super().__init__()
        self._basic_attack += 10
        self._max_hp = 100
        self._hp = 100
        self._hp_regeneration = 1
        self._max_mana = 500
        self._mana = 500
        self._mana_regeneration = 5
        self._spell_book = ElementalSpellBook()
        self._equipment = []

    def info(self):
        print("=" * 30)
        print("Your character")
        print(f"max_hp: {self._max_hp} \t max_mana: {self._max_mana}")
        print(f"hp: {self._hp} \t mana: {self._mana}")
        print(f"GOLD:  {self._gold}")
        print("=" * 30)

    def fight(self):
        while True:
            self.info()
            print("a - basic_attack")
            print("b - open ElementalSpellBook")
            inp = input("Choose an action (a/b) or 'q' to quit: ").lower()
            if inp == 'a':
                return self._basic_attack
            elif inp == 'b':
                return self._spell_book.choose_spell(self)
            elif inp == 'q':
                print("Exiting fight.")
                break
            else:
                print("Invalid choice. Please choose again.")

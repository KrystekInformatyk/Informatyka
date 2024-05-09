from characters.basic_character import BasicCharacter
from random import randint

class Goblin(BasicCharacter):
    def __init__(self) -> None:
        super().__init__()
        self._basic_attack = randint(1, 10)
        self._max_hp = 90
        self._hp = 90
        self._max_mana = 50
        self._mana = 50

    def fight(self):
        print("=" * 20)
        print("Evil goblin !!!")
        self.print_basic_statistics()
        return self._basic_attack

    def drop(self):
        return randint(10, 50)

    def info(self):
        print("=" * 30)
        print("Goblin stats")
        print(f"HP: {self._hp} / {self._max_hp}, Mana: {self._mana} / {self._max_mana}, Attack: {self._basic_attack}")
        print("=" * 30)

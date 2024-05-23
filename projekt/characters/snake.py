from characters.basic_character import BasicCharacter

class Snake(BasicCharacter):
    def __init__(self):
        super().__init__()
        self._name = "Snake"
        self._basic_attack += 5
        self._max_hp = 80
        self._hp = 80
        self._hp_regeneration = 1
        self._max_mana = 0  # Snakes do not use mana
        self._mana = 0
        self._mana_regeneration = 0

    def poison_bite(self, target):
        damage = 10
        print("Snake uses poison bite!")
        return damage

    def fight(self):
        return self.poison_bite(None)  # Assuming fight targets an opponent, replace None with actual target if needed

    def inf(self):
        print("="*30)
        print("Snake stats")
        print(f"HP: {self._hp} / {self._max_hp}")
        print("="*30)

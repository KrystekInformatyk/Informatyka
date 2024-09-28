from characters.basic_character import BasicCharacter

class Vampire(BasicCharacter):
    def __init__(self):
        super().__init__()
        self._name = "vampire"
        self._basic_attack += 15
        self._max_hp = 120
        self._hp = 120
        self._hp_regeneration = 2
        self._max_mana = 300
        self._mana = 300
        self._mana_regeneration = 3

    def bite(self, target):
        damage = 20
        print("Vampire bites draining life!")
        self._hp += damage // 2
        return damage

    def fight(self):
        return self.bite(None)  # Assuming fight targets an opponent, replace None with actual target if needed

    def inf(self):
        print("="*30)
        print("Vampire stats")
        print(f"HP: {self._hp} / {self._max_hp}, Mana: {self._mana} / {self._max_mana}")
        print("="*30)

class BasicCharacter:
    def __init__(self):
        self._is_alive = True
        self._gold = 0
        self._basic_attack = 0
        self._max_hp = 0
        self._hp = 0
        self._hp_regeneration = 0
        self._max_mana = 0
        self._mana = 0
        self._mana_regeneration = 0

    def print_basic_statistics(self):
        print("==" * 10)
        print(f"Max Hp = \t{self._max_hp} Max Mana = \t{self._max_mana}")
        print(f"Hp = \t{self._hp} Mana = \t{self._mana}")
        print("==" * 10)

    def basic_attack(self):
        return self._basic_attack

    def is_alive(self):
        return self._hp > 0

    def regenerate(self):
        if self._hp + self._hp_regeneration > self._max_hp:
            self._hp = self._max_hp
        else:
            self._hp += self._hp_regeneration

        if self._mana + self._mana_regeneration > self._max_mana:
            self._mana = self._max_mana
        else:
            self._mana += self._mana_regeneration

    def reduce_hp(self, damage):
        self._hp -= damage

    def add_gold(self, gold):
        self._gold += gold

    def drop(self):
        return self._gold

    def total_rest(self):
        self._hp = self._max_hp
        self._mana = self._max_mana

    def modify_attack(self):
        self._basic_attack += 1

    def modify_hp(self):
        self._max_hp += 1
        self._hp += 1

    def modify_hp_regeneration(self):
        self._hp_regeneration += 1

    def modify_mana(self):
        self._max_mana += 1
        self._mana += 1

    def modify_mana_regeneration(self):
        self._mana_regeneration += 1

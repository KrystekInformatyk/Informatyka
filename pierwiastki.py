class Pierwiastek:
    def __init__(self, nazwa, masa_atomowa, liczba_atomowa):
        self.masa_atomowa = masa_atomowa
        self.liczba_atomowa = liczba_atomowa
        self.nazwa = nazwa

    def wyswietl_info(self):
        print(
            f"Pierwiastek {self.nazwa}, masa atomowa {self.masa_atomowa},liczba atomowa  {self.liczba_atomowa}"
        )


Tytan = Pierwiastek("tytan", 48, 22)
Cyrkon = Pierwiastek("cyrkon", 91, 40)
German = Pierwiastek("german", 73, 32)
Tytan.wyswietl_info()
Cyrkon.wyswietl_info()
German.wyswietl_info()
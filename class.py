class Ludzik:
    def __init__(self, _orientacja_seksualna: str = "", _imie: str = "", _nazwisko: str = "", _płeć: str = "") -> None:
        self.orientacja_seksualna = _orientacja_seksualna
        self.imie = _imie
        self.nazwisko = _nazwisko
        self.płeć = _płeć

    def ludzik_info(self) -> None:
        print("Człowiek o imieniu", self.imie, ", nazwisku", self.nazwisko, ", płci", self.płeć, "i o orientacji sesualnej", self.orientacja_seksualna)


ludzik = Ludzik("Gay", "Antoniusz", "Garczyński", "Man")
ludzik.ludzik_info()

class Czołg:
    def __init__(self, _model: str = "", _przeznaczenie: str = "", _kraj_produkcji: str = "", _rok_wydania: str = "") -> None:
        self.model = _model
        self.przeznaczenie = _przeznaczenie
        self.kraj_produkcji = _kraj_produkcji
        self.rok_wydania = _rok_wydania

    def czołg_info(self) -> None:
        print("Czołg o modelu", self.model, ", przeznaczeniu", self.przeznaczenie, ", kraju produkcji", self.kraj_produkcji, "i o roku wydania", self.rok_wydania)


czołg = Czołg("Rudy 102", "mordowanie niewinnych cywili", "bośnia", "1669")
czołg.czołg_info()

class Laptop:
    def __init__(self, _karta_graficzna: str = "", _pamięć_ram: str = "", _procesor: str = "", _płyta_główna: str = "") -> None:
        self.karta_graficzna = _karta_graficzna
        self.pamięć_ram = _pamięć_ram
        self.procesor = _procesor
        self.płyta_główna = _płyta_główna

    def laptop_info(self) -> None:
        print("Laptop o karcie graficznej", self.karta_graficzna, ", pamięci ram", self.pamięć_ram, ", procesorze", self.procesor, "i o płycie głównej", self.płyta_główna)


laptop = Laptop("RTX 4090", "32,5 GB", "I10-15900KF", "ASUS 99-me celeron")
laptop.laptop_info()

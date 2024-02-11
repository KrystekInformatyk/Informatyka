class Kalkulator:
    @staticmethod
    def dodaj(a, b):
        return a + b
    
    @staticmethod
    def odejmij(a, b):
        return a - b
    
    @staticmethod
    def pomnoz(a, b):
        return a * b

    @staticmethod
    def podziel(a, b):
        if b == 0:
            raise ValueError("Nie można dzielić przez zero.")
        return a / b
    
    @staticmethod
    def potęga(a, b):
        return a ** b

# Przykłady użycia
wynik_dodawania = Kalkulator.dodaj(3, 5)
wynik_mnozenia = Kalkulator.pomnoz(3, 5)
wynik_odejmowania = Kalkulator.odejmij(3, 5)
wynik_dzielenia = Kalkulator.podziel(3, 5)
wynik_potęgowania = Kalkulator.potęga(3, 5)

print("Wynik dodawania:", wynik_dodawania)
print("Wynik mnożenia:", wynik_mnozenia)
print("Wynik odejmowania:", wynik_odejmowania)
print("Wynik dzielenia:", wynik_dzielenia)
print("Wynik potęgowania:", wynik_potęgowania)
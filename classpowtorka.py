# class Zegar:
#     def __init__(self, godzina:int, minuta, sekunda):
#         self.godzina = godzina
#         self.minuta = minuta
#         self.sekunda = sekunda

#     def zmien_godzine(self, godzina):
#         self.godzina = godzina

#     def wyswietl_info(self):
#         print(f"Godzina: {self.godzina}, Minuta: {self.minuta}, Sekunda: {self.sekunda}")

# zegar=Zegar(10, 53, 47)
# zegar.zmien_godzine(15)
# zegar.wyswietl_info()



class PierwszaA:
    def __init__(self, mikołaj, agnieszka, mateusz):
        self.mikolaj = mikołaj
        self.agnieszka = agnieszka
        self.mateusz = mateusz

    def opis(self):
        print(f"Wiek Mikołaja: {self.mikolaj}, Wiek Agnieszki {self.agnieszka}, wiek Mateusza: {self.mateusz}")

    def zmien_wiek_agnieszki(self, agnieszka):
        self.agnieszka = agnieszka

pierwszaA = PierwszaA(14, 15, 14)
pierwszaA.zmien_wiek_agnieszki(16)
pierwszaA.opis()
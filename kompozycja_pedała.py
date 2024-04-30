# class Pracownik:
#     def init(self, imie, nazwisko, pensja, ocena_pracy, doswiadczenie, podgrupa):
#         self.imie = imie
#         self.nazwisko = nazwisko
#         self.pensja = pensja
#         self.ocena_pracy = ocena_pracy
#         self.doswiadczenie = doswiadczenie
#         self.podgrupa = podgrupa

#     def zmien_pensje(self, nowa_pensja):
#         self.pensja = nowa_pensja

#     def zmien_ocene_pracy(self, nowa_ocena):
#         self.ocena_pracy = nowa_ocena

#     def zmien_doswiadczenie(self, nowe_doswiadczenie):
#         self.doswiadczenie = nowe_doswiadczenie

#     def opis(self):
#         print(f"Imię: {self.imie}")
#         print(f"Nazwisko: {self.nazwisko}")
#         print(f"Pensja: {self.pensja}")
#         print(f"Ocena pracy: {self.ocena_pracy}")
#         print(f"Doświadczenie: {self.doswiadczenie}")
#         print(f"Podgrupa: {self.podgrupa}")


# class Pracownik_Montazu(Pracownik):
#     def init(self, imie, nazwisko, pensja, ocena_pracy, doswiadczenie, podgrupa):
#         super().init(imie, nazwisko, pensja, ocena_pracy, doswiadczenie, podgrupa)


# class Pracownik_IT(Pracownik):
#     def init(self, imie, nazwisko, pensja, ocena_pracy, doswiadczenie, podgrupa):
#         super().init(imie, nazwisko, pensja, ocena_pracy, doswiadczenie, podgrupa)


# class Pracownik_Organizacji_Pracy(Pracownik):
#     def init(self, imie, nazwisko, pensja, ocena_pracy, doswiadczenie, podgrupa):
#         super().init(imie, nazwisko, pensja, ocena_pracy, doswiadczenie, podgrupa)


# #==============================================================================================
# pracownik1 = Pracownik_Montazu("Ben", "Smajher", 3500, 4, 3, "elektryk")
# pracownik2 = Pracownik_IT("Jay", "Ram", 5000, 5, 5, "programista")
# pracownik3 = Pracownik_Organizacji_Pracy("Maximov", "Vitalin", 4000, 3, 2, "mechanik")

# pracownik1.zmien_pensje(4000)
# pracownik1.opis()

class Pracownik:
    def __init__(self, imie, nazwisko, pensja, ocena_pracy, doswiadczenie, podgrupa):
        self.imie = imie
        self.nazwisko = nazwisko
        self.pensja = pensja
        self.ocena_pracy = ocena_pracy
        self.doswiadczenie = doswiadczenie
        self.podgrupa = podgrupa

    def zmien_pensje(self, nowa_pensja):
        self.pensja = nowa_pensja

    def zmien_ocene_pracy(self, nowa_ocena):
        self.ocena_pracy = nowa_ocena

    def zmien_doswiadczenie(self, nowe_doswiadczenie):
        self.doswiadczenie = nowe_doswiadczenie

    def opis(self):
        print(f"Imię: {self.imie}")
        print(f"Nazwisko: {self.nazwisko}")
        print(f"Pensja: {self.pensja}")
        print(f"Ocena pracy: {self.ocena_pracy}")
        print(f"Doświadczenie: {self.doswiadczenie}")
        print(f"Podgrupa: {self.podgrupa}")

class PracownikMontazu:
    def __init__(self, pracownik):
        self.pracownik = pracownik

    # Można dodać specyficzne dla montażu metody

class PracownikIT:
    def __init__(self, pracownik):
        self.pracownik = pracownik

    # Można dodać specyficzne dla IT metody

class PracownikOrganizacjiPracy:
    def __init__(self, pracownik):
        self.pracownik = pracownik

    # Można dodać specyficzne dla organizacji pracy metody

# Tworzenie obiektów pracowników
pracownik_bazowy1 = Pracownik("Ben", "Smajher", 3500, 4, 3, "elektryk")
pracownik_montazu = PracownikMontazu(pracownik_bazowy1)

pracownik_bazowy2 = Pracownik("Jay", "Ram", 5000, 5, 5, "programista")
pracownik_it = PracownikIT(pracownik_bazowy2)

pracownik_bazowy3 = Pracownik("Maximov", "Vitalin", 4000, 3, 2, "mechanik")
pracownik_organizacji_pracy = PracownikOrganizacjiPracy(pracownik_bazowy3)

# Zmiana pensji i wyświetlanie opisu dla pracownika montażu
pracownik_montazu.pracownik.zmien_pensje(4000)
pracownik_montazu.pracownik.opis()

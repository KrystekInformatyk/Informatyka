import uuid

def inf(lst: list) -> None:
    for ksiazka in lst:
        for key, value in ksiazka.items():
            print(f"{key}: {value}")
        print("---" * 10)

def dodaj_ksiazke() -> dict:
    nowa_ksiazka = {'id': str(uuid.uuid4())}
    nowa_ksiazka['tytul'] = input("Podaj tytuł książki: ")
    nowa_ksiazka['autor'] = input("Podaj autora książki: ")
    nowa_ksiazka['liczba_stron'] = int(input("Podaj liczbę stron książki: "))
    nowa_ksiazka['rok_wydania'] = int(input("Podaj rok wydania książki: "))
    return nowa_ksiazka

def usun_ksiazke(lst: list, id_do_usuniecia: str) -> None:
    for ksiazka in lst:
        if ksiazka['id'] == id_do_usuniecia:
            lst.remove(ksiazka)
            print("Książka usunięta z biblioteki.")
            return
    print("Nie znaleziono książki o podanym ID.")

def edycja(dc: dict) -> None:
    print("Wprowadź klucz, który chcesz edytować:")
    print("===" * 25)
    for k, v in dc.items():
        print(f"{k}: {v}")
    print("===" * 25)
    klucz_do_edytowania = input()
    if klucz_do_edytowania in dc:
        dc[klucz_do_edytowania] = input(f"Nowa wartość dla {klucz_do_edytowania}: ")
        print("Dane zaktualizowane.")
    else:
        print("Podany klucz nie istnieje.")

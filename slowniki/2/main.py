from functions import inf, edycja, dodaj_ksiazke, usun_ksiazke

biblioteka = [
    {'id': '1', 'tytul': 'Władca Pierścieni', 'autor': 'J.R.R. Tolkien', 'liczba_stron': 1200, 'rok_wydania': 1954},
    {'id': '2', 'tytul': 'Harry Potter', 'autor': 'J.K. Rowling', 'liczba_stron': 800, 'rok_wydania': 1997},
    {'id': '3', 'tytul': 'Złodziejka książek', 'autor': 'Markus Zusak', 'liczba_stron': 550, 'rok_wydania': 2005}
]

while True:
    print("==="*25)
    print("1 - informacje o książkach")
    print("2 - dodaj książkę")
    print("3 - usuń książkę")
    print("4 - edytuj dane książki")
    print("5 - wyjdź z programu")
    print("==="*25)

    inp = input().lower()

    if inp == "1":
        inf(biblioteka)
    elif inp == "2":
        nowa_ksiazka = dodaj_ksiazke()
        biblioteka.append(nowa_ksiazka)
        print("Książka dodana do biblioteki.")
    elif inp == "3":
        id_do_usuniecia = input("Podaj ID książki do usunięcia: ")
        usun_ksiazke(biblioteka, id_do_usuniecia)
    elif inp == "4":
        id_do_edytowania = input("Podaj ID książki do edycji: ")
        edytowana_ksiazka = inf(biblioteka, id_do_edytowania)
        edycja(edytowana_ksiazka)
        print("Dane książki zostały zaktualizowane.")
    elif inp == "5":
        print("Program zakończy działanie.")
        break
    else:
        print("Niepoprawna komenda")

from functions import inf, edycja

ksiazka = {
    'tytul': 'Władca Pierścieni',
    'autor': 'J.R.R. Tolkien',
    'liczba_stron': 1200,
    'rok_wydania': 1954
}

while True:
    print("==="*25)
    print("e - wyjdź z programu")
    print("i - informacje o książce")
    print("ed - edytuj dane")
    print("==="*25)
    inp = input().lower()
    if 'e' == inp:
        break
    elif 'i' == inp:
        inf(ksiazka)
    elif 'ed' == inp:
        edycja(ksiazka)
    else:
        print("Niepoprawna komenda")
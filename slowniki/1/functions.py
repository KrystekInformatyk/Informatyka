def inf(dc):
    for k, v in dc.items():
        print(f"{k}: {v}")


def edycja(dc):
    print("Wprowadź klucz, który chcesz edytować:")
    print("==="*25)
    inf(dc)
    print("==="*25)
    inp = input()
    dc[inp] = input("Podaj nowe dane:")
#1.Napisz program który przyjmie od użytkownika r i policzy V kuli. Wyświetl wynik na konsoli.
# import math

# print("Wprowadź promień kuli")
# r = int(input())

# v = 4*math.pi*r*r
# print()

#2.Napisz program który wyświetli n razy kocham programować. 
# n = int(input())
# while n > 0:
#     print(n*f"Kocham programować ")
#     n=-1
    
#3.Napisz program który sumuje liczby aż nie napisze się stop. Wyświetl wynik na konsoli.

while True:
    liczba = input("Podaj liczbę (wpisz 'stop' aby zakończyć): ")
    
    if liczba.lower() == 'stop':
        break
    
    try:
        liczba = float(liczba)
        suma += liczba
    except ValueError:
        print("To nie jest liczba! Spróbuj jeszcze raz.")

print(f"Suma wprowadzonych liczb wynosi: {suma}")

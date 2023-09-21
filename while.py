numbers = []

i = 0
while i < 5:
    try:
        number = float(input(f"Podaj liczbę {i + 1}: "))
        numbers.append(number)
        i += 1
    except ValueError:
        print("To nie jest liczba. Spróbuj ponownie.")


suma = sum(numbers)

najwieksza = max(numbers)

najmniejsza = min(numbers)

srednia = suma / len(numbers)

liczby_parzyste = [x for x in numbers if x % 2 == 0]
ilosc_parzystych = len(liczby_parzyste)

duplicates = []
for x in numbers:
    if numbers.count(x) > 1 and x not in duplicates:
        duplicates.append(x)

numbers = list(set(numbers))

squares = [x ** 2 for x in numbers]

print(f"Suma liczb: {suma}")
print(f"Największa liczba: {najwieksza}")
print(f"Najmniejsza liczba: {najmniejsza}")
print(f"Średnia arytmetyczna: {srednia}")
print(f"Ilość liczb parzystych: {ilosc_parzystych}")
print(f"Powtarzające się elementy: {duplicates}")
print(f"Lista bez powtórzeń: {numbers}")
print(f"Kwadraty liczb: {squares}")

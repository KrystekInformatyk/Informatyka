# 1. Wyświetl wszystkie liczby z listy "numbers" w odwrotnej kolejności.
print("9-=-"*10)
numbers = [1, 1, 1, 2, 2, 5]

i = -1
while i >= -len(numbers):
    print(numbers[i])
    i -= 1

# 2. Poproś użytkownika o podanie liczby. Sprawdź, czy liczba ta znajduje się w liście "numbers".
print("9-=-"*10)
numbers = [1, 1, 1, 2, 2, 5]
a = int(input())
if a in numbers:
    print("Tak")
else:
    print("Nie")

# 3. Wyświetl indeks pierwszego wystąpienia danej liczby w liście "numbers".
print("9-=-"*10)
numbers = [1, 1, 1, 2, 2, 5]
a = int(input())
i = 0
while i < len(numbers):
    if a == numbers[i]:
        print(i)
        break
    i += 1

# 4. Znajdź ilość liczb większych niż 10 w liście "numbers".
print("9-=-"*10)
numbers = [1, 1, 1, 2, 2, 5, 11]
ile = 0
i = 0
while i < len(numbers):
    if numbers[i] > 10:
        ile += 1
    i += 1
print(ile)

# 5. Posortuj listę "numbers" w kolejności malejącej.
print("9-=-"*10)
numbers = [11, 2, 10, 3, 1, 2, 4]
numbers.sort(reverse=True)
print(numbers)

# 6. Znajdź drugą największą liczbę w liście "numbers".
print("9-=-"*10)
numbers = [11, 2, 10, 3, 1, 2, 4, 11]

max1 = float('-inf')
max2 = float('-inf')

i = 0
while i < len(numbers):
    if numbers[i] > max1:
        max2 = max1
        max1 = numbers[i]
    elif numbers[i] > max2 and numbers[i] != max1:
        max2 = numbers[i]
    i += 1

print(f"max1 {max1}")
print(f"max2 {max2}")

# 7. Stwórz nową listę o nazwie "doubled_numbers" zawierającą podwojoną wartość każdej liczby z listy "numbers".
print("9-=-"*10)
numbers = [1, 1, 2, 2, 3, 3, 4, 4, 10, 10, 10, 10]
doubled_numbers = []

i = 0
while i < len(numbers):
    doubled_numbers.append(numbers[i] * 2)
    i += 1
print(doubled_numbers)

# 8. Zlicz ilość wystąpień danej liczby w liście "numbers".
print("9-=-"*10)
numbers = [1, 1, 2, 2, 3, 3, 4, 4, 10, 10, 10, 10]
a = float(input("-"))
ile = 0
i = 0
while i < len(numbers):
    if numbers[i] == a:
        ile += 1
    i += 1
print(ile)

# 9. Wyświetl wszystkie liczby z listy "numbers" z ich indeksami.
print("9-=-"*10)
numbers = [1, 1, 2, 2, 3, 3, 4, 4, 10, 10, 10, 10]

i = 0
while i < len(numbers):
    print(f"{i} {numbers[i]}")
    i += 1

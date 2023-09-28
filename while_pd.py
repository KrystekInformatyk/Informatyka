# 1. Stwórz pustą listę o nazwie "numbers".
print("1-=-"*10)
numbers = []
print(len(numbers))
print(numbers)

# 2. Poproś użytkownika o podanie 5 liczb i dodaj je do listy.
print("2-=-"*10)
print(numbers)

i = 0
while i < 5:
    a = float(input())
    numbers.append(a)
    print(numbers)
    i += 1

# 3. Oblicz sumę liczb znajdujących się w liście "numbers".
print("3-=-"*10)
numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(numbers)

suma = 0
i = 0
while i < len(numbers):
    suma += numbers[i]
    i += 1
print(f"{numbers} - suma = {suma}")

# 4. Znajdź największą liczbę w liście "numbers".
print("4-=-"*10)
numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

my_max = numbers[0]
i = 0
while i < len(numbers):
    if my_max < numbers[i]:
        my_max = numbers[i]
    i += 1
print(f"my_max = {my_max}")

# 5. Znajdź najmniejszą liczbę w liście "numbers".
print("5-=-"*10)
numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

my_min = numbers[0]
i = 0
while i < len(numbers):
    if my_min > numbers[i]:
        my_min = numbers[i]
    i += 1
print(f"my_min = {my_min}")

# 6. Policz średnią arytmetyczną liczb w liście "numbers".
print("6-=-"*10)
numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(numbers)

my_sum = 0
i = 0
while i < len(numbers):
    my_sum += numbers[i]
    i += 1
print(my_sum / len(numbers))

# 7. Znajdź ilość liczb parzystych w liście "numbers".
print("7-=-"*10)
numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

i = 0
parzyste = 0
while i < len(numbers):
    if numbers[i] % 2 == 0:
         parzyste += 1
   
# 8. Stwórz nową listę o nazwie "duplicates" zawierającą powtarzające się elementy z listy "numbers".
numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
duplicates = []
i = 0

while i < len(numbers):
    if numbers.count(numbers[i]) > 1 and numbers[i] not in duplicates:
        duplicates.append(numbers[i])
    i += 1
print(numbers)
print(duplicates)

# 9. Usuń wszystkie powtarzające się elementy z listy "numbers".
print("9-=-"*10)
numbers = [1, 1, 1, 2, 2, 5, 5, 5]
new_list = []

i = 0
while i < len(numbers):
    if numbers[i] not in new_list:
        new_list.append(numbers[i])
    i += 1
print(new_list)

# 10. Stwórz nową listę o nazwie "squares" zawierającą kwadraty liczb z listy "numbers".
print("10-=-"*10)
numbers = [1, 1, 1, 2, 2, 5]
squares = []
i = 0
while i < len(numbers):
    squares.append(numbers[i] ** 2)
    i += 1
print(squares)

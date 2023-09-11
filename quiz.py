print(" ")
print("Czy jesteś idiotą?")
print(" ")
print("Czy umiesz dotknąć łokcia językiem?")
print("A - tak     B - nie")

odp = input("Odp =")
sum = 0

if odp == "A":
  sum = sum + 0
if odp == "B":
  sum = sum + 1

if odp == "a":
  sum = sum + 0
if odp == "b":
  sum = sum + 1

print("Czy masz płatną licencję na winrara?")
print("A - tak     B - nie")

odp = input("Odp =")

if odp == "A":
  sum = sum + 0
if odp == "B":
  sum = sum + 1

if odp == "a":
  sum = sum + 0
if odp == "b":
  sum = sum + 1

print("Ile to 1:0?")
print("A - 1,45546838457     B - nie da się")

odp = input("Odp =")

if odp == "A":
  sum = sum + 0
if odp == "B":
  sum = sum + 1

if odp == "a":
  sum = sum + 0
if odp == "b":
  sum = sum + 1

if sum == 0:
  print("Jesteś skończonym idiotą, przykro mi"," Liczba punktów = ", sum)
elif sum == 3:
  print("Nie jesteś idiotą","Liczba punktów = ", sum)

elif sum > 0 < 3:
  print("Jesteś częściowym idiotą","Liczba punktów = ", sum)


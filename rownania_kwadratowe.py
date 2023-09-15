import math

while True:
    print("licz a | zamknij b")
    inp = input().upper()
    if inp == "a":
        b = float(input())
        a = float(input())
        c = float(input())

        delta = b**2 - 4*a*c
        if delta > 0:
            x1 = (-b-math.sqrt(delta))/(2*a)
            x2 = (-b-math.sqrt(delta))/(2*a)
            print(f"Mam 2 pierwiastki x1 = {x1} x2 = {x2}")
        elif delta == 0:
            x = -b/2*a
            print(f"x {x}")
        else:
            print("nie ma pierwiastków")
    elif inp == "B":
        break
    else: 
        print("Nie ma takiej komendy")
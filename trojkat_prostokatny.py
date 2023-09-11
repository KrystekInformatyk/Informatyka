import math

a = float(input())
b = float(input())
c = float(input())

if a + b > c and b + c > a and c + a > b:
    print("to jest trójkąt")
    p = 1/2*(a+b+c)
    p_po = math.sqrt(p*(p-a)*(p-b)*(p-c))
    print (p_po)
    if a**2 + b**2 == c**2 or c**2 + b**2 == b**2 or a**2 + c**2 == a**2:
        print("prostokątny")
    else:
        print("niet prostokąt")
else:
    print("to nie jest trojkąt")

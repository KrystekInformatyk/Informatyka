import math

print(" ")

print("Pola figur płaskich:")

print("Pole trójkąta")
a = float(input("bok a = "))
b = float(input("bok b = "))
c = float(input("bok c = "))


p = 0.5*(a+b+c)
P = math.sqrt(p*(p-a)*(p-b)*(p-c))
print(f"Pole = {P}")

print(" ")

print("Pola brył:")

print("Pole sześcianu")
d = float(input("krawędź sześcianu = "))


p = 6*d*d
print(f"Pole = {p}")

print(" ")

print("Pole prostopadłościanu")
e = float(input("krawedź ściany bocznej a = "))
f = float(input("krawedź ściany bocznej b = "))
g = float(input("krawedź podstawy = "))

p = 2*e*f+2*e*g+2*f*g
print(f"Pole = {p}")

print(" ")

print("Pole walca")
h = float(input("promień podstawy = "))
i = float(input("wysokość = "))
j = math.pi

p = 2*j*h*h+2*j*i
print(f"Pole = {p}")

print(" ")

print("Pole stożka")
k = float(input("promień podstawy = "))
l = float(input("przeciwprostokątna = "))
m = math.pi

p = m*(k+l)
print(f"Pole = {p}")

print(" ")

print("Pole kuli")
n = float(input("promień podstawy = "))
o = math.pi

p = 4*o*n*n
print(f"Pole = {p}")
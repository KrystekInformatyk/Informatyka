import math

def pole_prostokata(a, b):
    return a * b

def pole_kwadratu(a):
    return a ** 2

def pole_trojkata(a, h):
    return 0.5 * a * h

def pole_kola(r):
    return math.pi * r ** 2
  
def pole_trapezu(a, b, h):
    return 0.5 * (a + b) * h
  
def pole_rownolegloboku(a, b):
    return a * b

print("Pole prostokąta: ", pole_prostokata(4, 6))
print("Pole kwadratu: ", pole_kwadratu(5))
print("Pole trójkąta: ", pole_trojkata(3, 4))
print("Pole koła: ", pole_kola(2))
print("Pole trapezu: ", pole_trapezu(5, 7, 8))
print("Pole równoległoboku: ", pole_rownolegloboku(4, 5))

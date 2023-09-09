import math

print(" ")

co_mam_zrobić = input('Witaj w kalkulatorze! Jakie działanie mam wykonać? a - dodawanie ; b - odejmowanie ; c - mnożenie ; d - dzielenie ; e - pierwiastkowanie')
a = float(input('Podaj wartość A = '))
b = float(input('Podaj wartość B = '))

#zwykłe działania

if co_mam_zrobić == 'a':
    print(a+b)

if co_mam_zrobić == 'b':
    print(a-b)

if co_mam_zrobić == 'c':
    print(a*b)

if co_mam_zrobić == 'd':
    print(a/b)

#pierwiastkowanie

if co_mam_zrobić == 'e':
    co_mam_spierwiastkować = input('Jakie działanie mam spierwiastkować? a - dodawanie ; b - odejmowanie ; c - mnożenie ; d - dzielenie')

if co_mam_spierwiastkować == 'a':
    print(math.sqrt(a+b))

if co_mam_spierwiastkować == 'b':
    print(math.sqrt(a-b))

if co_mam_spierwiastkować == 'c':
    print(math.sqrt(a*b))

if co_mam_spierwiastkować == 'd':
    print(math.sqrt(a/b))


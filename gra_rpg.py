from random import randint, choice

print("Witaj w grze Chomik w Gangsterskiej Dżungli")

name = input('Podaj imie twojego chomika: ')
life = 100
siła = 100

print("Witaj", (name))

#ataki
def drapanie ():
    return randint(2,8)

def ugryzienie ():
    global siła
    if siła < 5:
        print("Nie masz wystarczająco siły!")
        return 0
    siła -= 5
    return randint(3,15)

def kopnij ():
    global siła
    if siła < 5:
        print("Nie masz wystarczająco siły!")
        return 0
    siła -= 5
    return randint(4, 12)

def orzech ():
    global siła
    if siła < 20:
        print("Nie masz wystarczająco siły!")
        return 0
    siła -= 20
    return randint(13, 30)

def wybierz_atak():
    print('A - Podrap')
    print('B - Ugryź')
    print('C - Kopnij')
    print('D - Super atak orzechem')
    co = input().upper()
    if co == 'A':
        return drapanie()
    elif co == 'B':
        return ugryzienie()
    elif co == 'C':
        return kopnij()
    elif co == 'D':
        return orzech()
    else:
        print("Nie wybrano akcji")
        return 0

#wrogowie
def rand_wrogowie():
    wrogowie = [
        ["Szczur", 20,6],
        ["Kot", 100,12],
        ["Mysz", 10, 3],
        ["Wąż", 15, 8],
        ["Jaszczurka", 10, 5]
    ]
    return choice(wrogowie)

liczba_pokonanych_przeciwników = 0


#-------------------------------------------------------------------------------

from random import randint, choice


# # ---------------------------------
# name = input('Podaj imie twojego bohatera: ')
# life = 100
# mana = 100


# # ---------------------------------
# def zwykly_atak():
#     return randint(3, 10)


# def fire_ball():
#     global mana
#     if mana < 10:
#         print("-"*40)
#         print("Nie masz wystarczającej ilości many!")
#         return 0
#     mana -= 10
#     return randint(13, 20)


# def wybierz_atak():
#     print('a/A - Wykonaj Normalny Atak')
#     print('b/B - Fire ball!')
#     co = input().upper()
#     if co == 'A':
#         return zwykly_atak()
#     elif co == 'B':
#         return fire_ball()
#     else:
#         print("Nie wybrano akcji")
#         return 0


# # ---------------------------------
# def random_oponent():
#     opponents = [
#         ["Mały Goblin", 15, 3, 0],
#         ["Nimfa Wodna", 10, 3, 0]
#     ]
#     return choice(opponents)


# # ---------------------------------
# liczba_pokonanych_przeciwników = 0


while life > 0:
    opponent = random_oponent()
    print("-"*40)


    while opponent[1] > 0 and life > 0:
        print(f"{name} walczy teraz z {opponent[0]}")
        print(f"Przeciwnik ma {opponent[1]} HP i zadaje Ci {opponent[2]} obrażeń")
       
        life -= opponent[2]
        if life <= 0:
            break


        print(f"Masz {life} HP i {mana} many")
        atak = wybierz_atak()
        opponent[1] -= atak
        print(f"Zadałeś {atak} obrażeń")


    if opponent[1] <= 0:
        print('Zabiłeś przeciwnika!!!')
        liczba_pokonanych_przeciwników += 1


print("-"*40)
print("KONIEC GRY!")
print(f"Zabiłeś {liczba_pokonanych_przeciwników} przeciwników")
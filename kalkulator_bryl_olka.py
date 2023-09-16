import math
import time
print('UWAGA! PROGRAM NIE PATRZY CZY PODANE LICZBY SPEŁNIAJĄ WYMAGANIA DANEGO POLA! NIE MAM OCHOTY TEGO PROGRAMOWAĆ. Pozdrawiam serdecznie.')
time.sleep(1)
print('Witaj w kalkulatorze!')
print('Kalkulator został zrobiony przez:')
time.sleep(1)
print('Olka :)')
print('Proszę nie kraść. Dziękuję')
time.sleep(1)
print('Zaraz będziesz musiał odpowiedzieć na kilka pytań zadanych przez program. W podanych pytaniach odpowiadać możesz tylko za pomocą liczb. Jeżeli podasz literę program nie zadziała.')
print('Mówiąc krócej: dajesz literę = wyjdą ci pierdoły')
time.sleep(1)
print('Odpowiedzi:')


a = float(input("a = "))
b = float(input("b = "))
c = float(input("c = "))
d = float(input("d = "))
h = float(input("h = "))
r = float(input("r = "))
H = float(input("H = "))
Pp = float(input("Pole powierzchni = "))
time.sleep(0.5)
print('Dziękuję za odpowiedź. Proszę czekać.')
time.sleep(0.1)
print('...')
time.sleep(0.1)
print('..')
time.sleep(0.1)
print('.')
time.sleep(0.2)


ppowszesci = 6*(a * a)
ppowprosto = 2*(a*b) + 2*(a*c) + 2*(b*c)
objetoscszesci = a*a*a
objetoscprosto = a*b*c
objetosckuli = 4/3*math.pi * (r*r*r)
objetoscwalca = math.pi * (r*r) * H
objetoscstozka = 1/3 * math.pi * (r*r) * H
objetoscostro = 1/3 * Pp * H
obwodkwadr = 4*a
obwodprosto = 2*(a) + 2*(b)
obwodrownoleglo = 2*a + 2*b
obwodtrap = a+b+c+d
obwodtroj = a+b+c
obwtrojrown = 3*a
obwromb = 4*a
polekwadr = a*a
poleprost = a*b
poletroj = 0.5*(a*h)
przekatnakwadr = a * math.sqrt(2)
poletrap = (a+b*h)/2

print('Wybierz co chcesz obliczyć z podanych liczb:')
time.sleep(1)
print('Najpierw wybierz czy ma to być pole/pole powierzchni (na pole powierchni wpisz "powierzchni"), obwód (wpisz "obwod"), objętość (wpisz "objetosc"), przekątna (wpisz "przekatna")')
print('Możesz również sprawdzić czy twoje boki mogą być trójkątem (wpisz "trojkat")')
odp1 = input()
if odp1 == 'pole':
    print('Wybrałeś pola. Teraz wybierz jakie pole ma to być')
    time.sleep(1)
    print('Dostępne pola: pole kwadratu (wpisz "kwadratu"), pole prostokąta (wpisz "prostokata"), pole trójkąta (wpisz "trojkata), pole tapezu (wpisz "trapez")')
    odppola = input()
    if odppola == 'kwadratu':
        print('Oto twoje pole:',polekwadr)
    elif odppola == 'prostokata':
        print('Oto twoje pole:',poleprost)
    elif odppola == 'trojkata':
        print('Oto twoje pole:',poletroj)
    elif odppola == 'trapez':
        print('Oto twoje pole:',poletrap)
    else:
        print('Nie ma takiej opcji. Wyłączanie programu.')
        time.sleep(0.3)
        print('...')
        time.sleep(0.2)
        print('..')
        time.sleep(0.2)
        print('.')
elif odp1 == 'powierzchni':
    print('Wybrałeś pole powierzchni. Teraz wybierz jakie pole powierzchni chcesz obliczyć.')
    time.sleep(1)
    print('Dostępne pola powierzchni: pole powierzchni szescianu (wpisz "szescian") oraz pole powierzchni prostopadłościanu (wpisz "prostopadloscian")')
    odppowierzchni = input()
    if odppowierzchni == 'szescian':
        print('Oto twoje pole powierzchni:',ppowszesci)
    elif odppowierzchni == 'prostopadloscian':
        print('Oto twoje pole powierzchni:',ppowprosto)
    else:
        print('Nie ma takiej opcji. Wyłączanie programu.')
        time.sleep(0.3)
        print('...')
        time.sleep(0.2)
        print('..')
        time.sleep(0.2)
        print('.')
elif odp1 == 'obwod':
    print('Wybrałeś obwód. Teraz wybierz jaki obwód ma to być.')
    time.sleep(1)
    print('Dostępne obwody: obwód kwadratu (wpisz "kwadrat"), obwód prostokąta (wpisz "prostokat"), obwód równoległoboku (wpisz "rownoleglobok"), obwód trapezu (wpisz "trapez"), obwód trójkąta (Wpisz "trojkat") i obwód trójkąta równobocznego (wpisz "trojkatrown")')
    odpobwod = input()
    if odpobwod == 'kwadrat':
        print('Oto twój obwód:',obwodkwadr)
    elif odpobwod == 'prostokat':
        print('Oto twój obwód:',obwodprosto)
    elif odpobwod == 'rownoleglobok':
        print('Otwo twój obwód:',obwodrownoleglo)
    elif odpobwod == 'trapez':
        print('Oto twój obwód:',obwodtrap)
    elif odpobwod == 'trojkat':
        print('Oto twój obwód:',obwodtroj)
    elif odpobwod == 'trojkatrown':
        print('Oto twój obwód:',obwtrojrown)
    else:
        print('Nie ma takiej opcji. Wyłączanie programu.')
        time.sleep(0.3)
        print('...')
        time.sleep(0.2)
        print('..')
        time.sleep(0.2)
        print('.')
elif odp1 == 'objetosc':
    print('Wybrałeś objętość. Teraz wybierz jaka objętość ma to być.')
    time.sleep(1)
    print('Dostępne objętości: objętość prostopadłościanu (wpisz "prostopadloscian"), objętość sześcianu (wpisz "szescian"), objętość kuli (wpisz "kula"), objętośc walca (wpisz "walec"), objętość stożka (wpisz "stożek"), pole ostorsłupa (wpisz "ostroslup")')
    odpobjetosc = input()
    if odpobjetosc == 'prostopadloscian':
        print('Oto twoja objętość:',objetoscprosto)
    elif odpobjetosc == 'szescian':
        print('Oto twoja objętość:',objetoscszesci)
    elif odpobjetosc == 'kuli':
        print('Oto twoja objętość',objetosckuli)
    elif odpobjetosc == 'walec':
        print('Oto twoja objętość:',objetoscwalca)
    elif odpobjetosc == 'stozek':
        print('Oto twoja objetość:',objetoscstozka)
    elif odpobjetosc == 'ostroslup':
        print('Oto twoja objętość:',objetoscostro)
    else:
        print('Nie ma takiej opcji. Wyłączanie programu.')
        time.sleep(0.3)
        print('...')
        time.sleep(0.2)
        print('..')
        time.sleep(0.2)
        print('.')
elif odp1 == 'przekatna':
    print('Wybrałeś przekątne. Teraz wybierz jaka przekątna ma to być.')
    time.sleep(1)
    print('Dostępne przekątne: przekątna kwadratu (wpisz "kwadrat")')
    odpprzekatne = input()
    if odpprzekatne == 'kwadrat':
        print('Oto twoja przekątna:',przekatnakwadr)
    else:
        print('Nie ma takiej opcji. Wyłączanie programu.')
elif odp1 == 'trojkat':
    if a + b > c and c + a > b and b + c > a:
        print('Twój trójkąt jest prawidłowy!')
    else:
        print('Twój trójkąt NIE jest prawidłowy.')
else:
    print('Niestety, ale nie ma takiej opcji w moim kalkulatorze. Możesz zawnioskować o dodanie wzoru poprzez kontakt ze mną na lekcji informatyki ;)')
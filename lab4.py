# Laboratorium 4
"""Michal Stefaniuk grupa Sroda 15;30 - 17;45"""

import random
#Zadanie1
"""Proszę utworzyć funkcję przyjmującą jeden parametr i zwracającą słownik. Liczba elementów w słowniku jest
wartością losową z przedziału [0,20). Kluczami są wartości rzeczywiste z przedziału [0, 1), a wartościami są
wartości wyrażenia matematycznego z jedną zmienną przekazanego jako parametr wywołania funkcji obliczone dla
danego klucza. Wartości w słowniku mają być zaokrąglone do trzeciego miejsca po przecinku i zapisane z taką dokładnością jako ciągi znaków (1p)"""

def fun1(a):
    s = {}
    rozmiar = random.randrange(0, 20)
    for i in range(rozmiar):
        klucz = random.random()
        s["{0:.3g}".format(klucz)] = "{0:.3g}".format(eval(a.format(klucz)))
    return s

#Zadanie2
"""Proszę napisać funkcję, do której można przekazać dowolną liczbę list i krotek a zwracającą listę zawierającą
 elementy wspólne dla wszystkich parametrów. Proszę użyć konstrukcji for-else (1p)"""

def fun2(*a):
    temp = []
    for item in a[0]:
        for seq in a[1:]:
            if item not in seq:
                break
        else:
            temp.append(item)
    return temp

#Zadanie3
"""Proszę napisać funkcję przyjmującą dwie sekwencje i parametr z wartością domyślną True. Funkcja zwraca listę zawierającą
 dwuelementowe krotki zawierające elementy o jednakowych indeksach z obu sekwencji. Jeżeli wartość trzeciego parametru wynosi 
 True, długość zwracanej listy równa jest długości krótszej z przekazanych sekwencji, w przeciwnym wypadku brakujące wartości 
 uzupełniamy wartością None. Budowanie każdej z wynikowych list jedna linijka! (2p)"""

def fun3(sekOne, sekTwo, flag=True):
    if flag:
        return [(sekOne[i], sekTwo[i]) for i in range(min(len(sekOne), len(sekTwo)))]
    else:
        return [(sekOne[i], sekTwo[i]) if i < min(len(sekOne), len(sekTwo)) else (sekOne[i], None) if len(sekOne) > len(sekTwo) else (None, sekTwo[i]) for i in range(max(len(sekOne), len(sekTwo)))]

#Zadanie4
"""Proszę napisać funkcję przyjmującą zmienną liczbę argumentów, która będzie zwracała najmniejszą/największą wartość. Następnie 
proszę napisać funkcję, przyjmującą jako parametry funkcję oraz zmienną liczba parametrów pozycyjnych. W wywołaniu proszę
przekazać funkcję szukającą min/max oraz listę. (2p)"""

def fun4(*arg):
    return min(*arg)

def fun5(function, *arg):
    return function(*arg)

#Zadanie5
"""Proszę napisać funkcję umożliwiającą rozmienienie kwoty pieniędzy przekazanej jako jej pierwszy parametr nominałami określonymi poprzez drugi parametr - 
wartość domyślna krotka (10,5,2)  (algorytm zachłanny). Proszę sprawdzić działanie funkcji przekazując inny zestaw monet. (2p)"""

def fun6(value, coins=(10, 5, 2)):
    coinArray = []
    for i in coins:
        while(value >= i):
            value = value - i
            coinArray.append(i)
    if value == 0:
        return coinArray
    else:
        return "nie da sie rozmienic podanej kwoty"

#Zadanie6
"""Proszę napisać funkcję przyjmującą cztery parametry: liczba, której wartość zgadujemy, granice przedziału, w którym szukana liczba się mieści i ostatni 
określający sposób poszukiwania wartości z wartością domyślną 'r'. Przy wartości domyślnej ostatniego parametru, liczby poszukujemy losując kolejną wartość,
 w innym przypadku poszukujemy wartości poprzez podział przedziału poszukiwania wartości na pół. W obu przypadkach w każdym kroku odpowiednio zawężamy 
 przedział poszukiwania (proszę wykorzystać operator trójargumentowy). Proszę sprawdzić ile kroków jest potrzebnych do znalezienia szukanej 
 wartości w zależności od metody. (2p)"""

def fun7(number, start, end, method='r'):
	if not start <= number <= end:
		return 'false arguments'
	counter = 0
	while True:
		guess = random.randint(start, end) if method == 'r' else (start + end) // 2
		counter += 1
		if guess == number:
			return counter
		else:
			start, end = (guess , end) if guess < number else (start, guess )
print(fun7(30,20,60,'r'))


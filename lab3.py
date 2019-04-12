# sample choice shuffle seed
from random import randrange
from sys import argv

#Zad 1
"""Proszę napisać funkcję sprawdzającą czy liczba przekazana jako parametr jej wywołania jest liczbą palindromową (2p)"""
def palindrom(arg):
    return (str(arg)==str(arg)[::-1])
   

#Zad 2
"""Proszę utworzyć słownik zawierający 100 elementów, w którym klucze są wartościami losowymi z przedziału [100,10000]; 
jeżeli w słowniku istnieje już klucz równy wylosowanej wartości nic nie robimy w przeciwnym wypadku dodajemy do słownika 
element (klucz: palindrom), gdzie palindrom=True/False (1p)"""

FirstDict = {}
count = 0
while count < 100:
    x=randrange(100,10000)
    if x not in FirstDict:
        FirstDict[x]=palindrom(x)
        count=count+1

#Zad 3
"""Proszę utworzyć listę stu wartości losowych z przedziału [0,20). Następnie na podstawie tej listy proszę utworzyć dwa słowniki:
 pierwszy - klucze wartości parzyste z listy, drugi - nieparzyste; w obu wartości - lista indeksów (określonych iteracyjnie) danego 
 klucza w liście. 
 
 Następnie na podstawie jednego z otrzymanych słowników proszę utworzyć nowy słownik, w którym klucze zostają takie 
 same jak w słowniku wejściowym, wartości tworzymy natomiast w sposób następujący: jeżeli lista będąca wartością związaną z danym 
 kluczem zawiera jakieś wartości podzielne bez reszty przez 3 ich lista stanowi wartość związaną z kluczem w nowym słowniku, jeżeli 
 takich liczb nie ma wartość jest krotką(maksymalny indeks[, minimalny indeks]) (2p)"""

ListOfRands = [randrange(0,20) for _ in range(100)]
EvenDict = {}
NotEvenDict = {}

for i,j in enumerate(ListOfRands):
    if j%2==0:
        EvenDict.setdefault(j,[]).append(i)
    else:
        NotEvenDict.setdefault(j,[]).append(i)


NewDict = { k:w if [j for j in w if j%3==0] else (max(w),min(w)) for k,w in EvenDict.items()}

#Zad 4
"""Proszę utworzyć słownik o rozmiarze równym wartości pierwszego parametru przekazanego do programu. Kluczami w tym słowniku mają być 
kolejne wartości naturalne, a wartościami liczby losowe z przedziału [2,15). Następnie proszę na jego podstawie utworzyć listę, której 
elementami są krotki (wartość, klucz) oraz słownik, w którym zostaną zamienione miejscami wartości z kluczami (2p)"""


InputDict = {i:randrange(2,15) for i in range(int(argv[1]))}
InputList = [(InputDict[i],i) for i in InputDict]
InputDictReverse = {InputDict[i]:i for i in InputDict}

#Zad 5
"""Proszę utworzyć listę 100 wartości losowych z przedziału [0,11). 
Następnie proszę na jej podstawie utworzyć słownik, 
w którym kluczami będą wartości z przedziału, z którego liczby były losowane, wartościami będą natomiast listy z indeksami
 (określonymi z wykorzystaniem metod setdefault i index) ich wystąpień w"""

ListOfRands = [randrange(0,11) for i in range(100)]
DictFromList = {}
for i in ListOfRands:
    DictFromList.setdefault(i,[]).append(ListOfRands.index(i,DictFromList[i][-1]+1 if DictFromList[i] else 0)) # ERROR BRAK DRUGIEGO ARGUMENTU
print(DictFromList)

#Zad 6
"""Proszę utworzyć dwa słowniki o rozmiarze 10, w których kluczami są kolejne wartości naturalne, a wartościami liczby losowe z przedziału [1,100). 
Następnie w obu słownikach proszę zamienić miejscami klucze z wartościami. Na podstawie tak otrzymanych słowników proszę utworzyć nowy słownik, 
w którym klucze są kluczami występującymi w obu wcześniej utworzonych słownikach, wartościami natomiast są dwuelementowe krotki wartości związanych 
z danym kluczem w słownikach oryginalnych (2p)"""

FirstDict = { i:randrange(0,100) for i in range(10) }
SecondDict = { i:randrange(0,100) for i in range(10)}

FirstDictSwap = { FirstDict[i]:i for i in FirstDict }
SecondDictSwap = {SecondDict[i]:i for i in SecondDict}

ThirdDict = { i:(FirstDictSwap[i],SecondDictSwap[i]) for i in SecondDictSwap if i in FirstDictSwap}

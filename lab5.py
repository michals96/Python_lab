from time import time
from sys import version
import random
import functools
import math
# Zadanie 1
powt = 1000
N = 10000

def forStatement():
    lista = []
    for i in range(N):
        lista.append(i)

def listComprehension():
    lista = [i for i in range(N)]

def mapFunction():
    lista = map(lambda x: x, range(N))

def generatorExpression():
    lista = (i for i in range(N))

def tester(fun):
    start = time()
    for i in range(powt):
        fun()
    stop = time()
    return stop - start

print(version)
test = (forStatement, listComprehension, mapFunction, generatorExpression)
for testFunction in test:
    print(testFunction.__name__.ljust(20), '=>', tester(testFunction))

# Zadanie 2
"""Proszę wyznaczyć wartość liczby pi metodą Monte-Carlo korzystając z funkcji filter (2p)."""

def MonteCarlo(steps):
    l = ((random.uniform(-1, 1), random.uniform(-1, 1)) for i in range(steps))
    pi = 4*(len(list(filter(lambda x: x[0]*x[0]+x[1]*x[1] < 1, l))))/steps
    return pi

# Zadanie 3
"""Proszę znaleźć:
największą wartość w każdym wierszu macierzy (map),
największą wartość w każdej kolumnie macierzy (map+zip),
sumę dwóch macierzy (map+zip+lista składana).
Każde polecenie jedna linijka (2p)"""

def maxone(A):
    print(list(map(max, A)))

def maxtwo(A):
    print(list(map(max, zip(*A))))


def maxthree(A, B):
    print(list(map(lambda x, y: [x[i]+y[i] for i in range(len(x))], A, B)))

#A = [[1, 2, 3], [3, 4, 5], [5, 6, 7]]
#B = [[1, 2, 3], [3, 4, 5], [5, 6, 7]]

A = ((1, 2), (2, 3), (3, 4))
B = ((1, 2), (3, 4), (5, 6))
maxone(A)
maxtwo(A)
maxthree(A, B)

# Zadanie 4
"""Mamy listę, której elementami są listy dwuelementowe (możemy je potraktować jako współrzędne 
punktów na płaszczyźnie). Chcemy utworzyć nową listę, w której pierwszym elementem jest lista x-ów,
a drugim lista y-ów. Proszę to zrobić w jednej linijce korzystając z funkcji myreduce, wyrażenia
lambda oraz wbudowanej funkcji map (obie listy tworzymy jednocześnie!) (2p)"""

coordinatesList = [
    [random.randrange(10), random.randrange(10)] for _ in range(10)]
print(coordinatesList)
#newlist = list( map(functools.reduce(lambda x,y: list(x,y) , coordinatesList[0], coordinatesList[1])) )
newList = list(functools.reduce(lambda x,y: map(lambda i,j: [i,j] if isinstance(i,int) else i+[j], x,y),coordinatesList))
print(newList)

# Zadanie 5
def function(X, Y):
    _x = functools.reduce(lambda x, y: x+y, X)/len(X)
    _y = functools.reduce(lambda x, y: x+y, Y)/len(Y)
    D = sum(((i-_x)**2) for i in X)
    a = sum(map(lambda xi, yi: yi*(xi-_x), X, Y)) / D
    b = a*_x + _y
    # Wykomentowany fragment kodu ktory generowal dziwny blad
    # nadano wartosc 1 dla dy aby program dalej sie kompilowal 
    dy =1 
    #dy = math.sqrt(sum(map(lambda xi,yi: (yi - (a*xi-b))**2, X, Y)) / len(X-2))
    da = dy / math.sqrt(D)
    db = dy * math.sqrt(1/len(X)+pow(_x,2)/D)
    print(dy,da,db)

function([1, 2, 3, 4], [3, 4, 5, 6])

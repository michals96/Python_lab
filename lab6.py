import math
# Zad1


def fun1():
    i = 1
    while True:
        yield i
        i += 1


def fun2(seq):
    for i in seq:
        if i == sum(filter(lambda k: not i % k, (x for x in range(1, i//2+1)))):
            yield i


def fun3(seq, val):
    for el in seq:
        if el <= val:
            yield el
        else:
            break


# Korzystając ze zdefiniowanych funkcji proszę wypisać doskonałe liczby naturalne mniejsze od 10000
'''for i in fun2(fun3(fun1(), 10000)):
    print(i)'''

# Zad2


def fun4(k):
    a = 0.05
    u = 0.0
    x = 1.0
    while x < k:
        u += a/x
        x += a
        yield x, u, math.log(x)


for i in fun4(1.5):
    print(i)

'''Każdą liczbę całkowitą można zapisać jako sumę wartości całkowitych mniejszych od niej samej,
np. 4 można zapisać jako: 1+1+1+1, 1+1+2, 1+3 oraz 2+2.
 Proszę napisać generator zwracający wszystkie możliwe sumy dla określonej wartości n (2p).'''
# Zad3

def fun5(arg):
    suma = 1
    licznik = 1
    while True:
        if(suma != arg+1):
            yield licznik
            suma = suma+licznik
        else:
            break

for i in fun5(10):
    print(i)


'''Proszę napisać generator zwracający przybliżenie funkcji sinus, gdzie kolejny wyraz wynosi:
(-1)**k*x**(1+2*k)/(1+2*k)!.
Proszę sprawdzić ile wyrazów ciągu jest koniecznych do uzyskania zadanej dokładności, np. 10-8 (2p).'''
# Zad4


def sinus(x):
    z = 0
    k = 0
    while True:
        z += ((-1)**k*x**(1+2*k))/math.factorial(1+2*k)
        yield z
        k += 1


for i, j in enumerate(sinus(math.pi)):
    if(abs(j - math.sin(math.pi)) < 1e-8):
        print("Przyblizenie sinusa", j, i)
        break


# Zad5
'''Proszę napisać generator działający dokładnie tak samo jak wbudowany range
(proszę się upewnić, że wiecie Państwo jak on działa!), ale pozwalający na generowanie liczb rzeczywistych (2p).'''


def range(start, stop=None, step=1):
    if stop is None:
        if start < 0:
            it = start+1
            while it <= 0:
                yield it
                it = it+1
        else:
            it = 0
            while it < start:
                yield it
                it = it+1
    elif stop < start and step > 0:
        it = start
        while it > stop:
            yield it
            it = it-step
    elif stop < start and step < 0:
        if step == 1:
            it = start
            while it > stop:
                yield it
                it = it+step
    elif stop > start and step > 0:
        it = start
        while it < stop:
            yield it
            it = it+step
    elif stop > start:
        if step == 1:
            it = start
            while it < stop:
                yield it
                it = it-step


''' Przypadki TESTOWE '''
# for el in range(8):
# print(el)

# for el in range(-8):
# print(el)

# for el in range(1, 8):
# print(el)

# for el in range(8, 1):
# print(el)

# for el in range(1, 8, 2):
# print(el)

# for el in range(1, 8, -2):
# print(el)

# for el in range(8, 1, 2):
# print(el)

# for el in range(8, 1, -2):
# print(el)

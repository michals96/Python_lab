#usr/bin/env/ python3
from __future__ import division 
import keyword
import math 
from copy import deepcopy
# do kopiowania wartosci a nie referencji
print ('Hello world')
a=1
b='a'
c="a"
d=1.3
print(type(a),type(b),type(c),type(d))
a,b=1,2
print(a,b)
a,b=b,a
print(a,b)
a,*b=1,2,3,4
print(a,b,type(b))
a = 3/2 # w pythonie2 to jest 1, a w python3 to jest 1.5
# zeby dokonac dzielenia calkowitego w python 3 robimy 3//2
print(keyword.kwlist)
print(dir(math)) # wyswietl zawartosc modulu
# help(math.modf) lub math.modf __doc__
# sum to /math.fsum
# abs to /math.fabs
# pow to /math.pow
k=(1,[1,'k',2],'s',(1,2,3))
#indeksujemy od 0 do dlugosc-1
print(type(k))
print(k)
print(len(k))#zwraca dlugosc
#ostatni element ma indeks len-1 lub -1
# pierwszy element ma indeks 0 lub -len
# k[1]=7 ERROR! krotki sa niemodyfikowalne
k[1][1]=7 # mozemy modyfikowac modyfikowalne elementy krotki
print(k)
temp = [1,2,3,]
s = temp
print((temp is s)) # is porownuje referencje
print(id(temp))#id pokazuje referencje 
print(id(s))

#if l is k
#	print('tak')
#l =k[1:17]  -> do l kopiuje elementy od 1 do 17 z k
#l =k[:17] -> od 1 do 16 wlacznie
#l =k[1:] -> od 1 do konca
#l =k[:] -> wszystko do konca
#l =k[:2] -> wszystko do konca co drugi
print('\n')
s=temp[:]
print(id(temp))#id pokazuje referencje 
print(id(s))# jak widac jest ona inna niz przy jawnym przypisaniu
# /////////////////
temp=k[:]
temp[1][1]=3
print('\n')
print(temp)
print(k)
# powyzsze modyfikacje nie tylko zmienaja kopie temp
# ale takze oryginal k dlatego jest to nie wygodne
l=[0]*15
l[2]=3
print(l)
l=[[]]*15
l[2].append(3)
print(l)
l=[[] for _ in range(15)] # dzieki temu listy sa od siebie niezalezne 
l[2].append((3,4,5,))
print(l)
l[2].extend((3,4,5,))
print(l)
# testowanie ifow do wartosci
a=1 if 1==2 else 3
print(a)

#funkcja kwadratowa
a=10
b=1
c=0

delta = b*b-4*a*c
if delta>0:
	deltasqrt=math.sqrt(delta)
	x1=(-b-deltasqrt)/2*a
	x2=(b-deltasqrt)/2*a
	print('Dwa pierwiastki ',x1,x2)
elif delta<0:
	print('brak pierwiastkow')
else:
	x1=(-b/2*a)
	print('Jeden pierwiastek ',x1)
# napisz from math import sqrt zeby pisac 
# sqrt a nie math.sqrt
# from cmath import sqrt -> oblicza pierwiastek z liczb zespolonych
# natomiast piszac takie dwie linie wykona sie ta
# aktualna czyli z cmath, zeby tego uniknac uzywaj is
# from cmath import sqrt as csqrt -> teraz obie dzialaja

#funkcja kwadratowa z zespolonymi
from cmath import sqrt as csqrt
a=10
b=1
c=0

delta = b*b-4*a*c
if delta>0:
	deltasqrt=csqrt(delta)
	x1=(-b-deltasqrt)/2*a
	x2=(b-deltasqrt)/2*a
	print('Dwa pierwiastki ',x1,x2)
elif delta<0:
	print('brak pierwiastkow')
else:
	x1=(-b/2*a)
	print('Jeden pierwiastek ',x1)
#input('') wczytywanie z klawiatury
from sys import argv
print(type(argv))
print(dir(argv))
#range(a) -> [a:a]
#range(a,b) -> [a:b]
#range(a,b,c) -> [a,a+c,...,b]
#
# PETLE
#
l=[1,2,33,4,5]
for i in l:
	i+=1
print(l)
for i in range(len(l)):
	l[i]+=1
print(l)
for i,el in enumerate(l): # enumerate zwraca indeks+element
	l[i]=el+1
print(l)

for i in range(10):
	if i>5:
		break
	else:
		print('?')

import string
from sys import argv

#zadanie1
if(len(argv)==1):
    print("Za malo argumentow")
else:
    x=argv[1:]
    y=''.join(x)
print("****ZAD1****")
print("INPUT: ",y)

#zadanie2
l1 = [i for i in y if i.islower()]
l2 = [i for i in y if i.isupper()]
l3 = [i for i in y if i.isnumeric()]
l4 = [i for i in y if i.isalpha()]
print("\n****ZAD2****")
print("MALE LITERY: ",l1)
print("DUZE LITERY: ",l2)
print("NUMERYCZNE: ",l3)
print("NIENUMERYCZNE: ",l4)

#zadanie3
l5 =[]
for i in l1:
    if i not in l5:
        l5.append(i)
l6=[(i,y.count(i)) for i in l5]
print("\n****ZAD3****")
print("BEZ POWTORZEN: ",l5)
print("DWUEL. KROTKA: ",l6)

#zadanie4
l6.sort(key = lambda x:x[1])
print("\n****ZAD4****")
print("POSORTOWANA DWUEL. KR. : ",l6)

#zadanie5
samogl=['a','e','u','y','i','o']
l7=[i.lower() for i in y if i.isalpha()]
count=0
for i in samogl:
    count += l7.count(i)
count2 = len(l1)+len(l2)-count
l8=[(int(i),count*int(i)+count2) for i in l3]
print("\n****ZAD5****")
print("LISTA DWUEL. KR. : ",l8)

#zadanie6
sumx = sum(i for i,j in l8) 
sumy = sum(j for i,j in l8)
avgx = sumx / len(l8)
avgy = sumy / len(l8)
D=sum((i-avgx)**2 for i,j in l8)
a=(1/D)*sum(j*(i-avgx) for i,j in l8)
b=avgy-a*avgx

print("\n****ZAD6****")
print("NAJMNIEJSZE KWADRATY:")
print("a = ",a,"b = ",b,"D =",D,"\n")










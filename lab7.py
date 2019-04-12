import glob
import keyword
import statistics
##### ******************************************************************** #####
                                    # ZADANIE 1
##### ******************************************************************** #####
'''Proszę napisać funkcję, która pozwoli na wypisanie: 
n początkowych wierszy pliku, 
n końcowych wierszy pliku, 
co n-tego wiersza pliku, 
n-tego słowa w wierszu i 
n-tego znaku w wierszu. 
Nazwę pliku oraz n przekazujemy jako parametr. Każdy podpunkt==jedna linia kodu (2p).'''


def fun1(file, n):
    with open(file) as fl:
        newList = fl.readlines()
        listOne = newList[:n]
        listTwo = newList[::n]
        listThree = newList[-n:]
        listFour = [i.split()[n-1] for i in newList if len(i.split()) >= n]
        listFive = [i[n-1] for i in newList if len(i) >= n]
        return listOne, listTwo, listThree, listFour, listFive
# print(fun1('/Users/michal/Desktop/pythonlab7/file.txt',2))


##### ******************************************************************** #####
                                     # ZADANIE 2
##### ******************************************************************** #####
'''Proszę napisać funkcję pozwalającą na wyświetlenie numerów wierszy w plikach z rozszerzeniem py, 
zawierających słowa kluczowe języka z uwzględnieniem i bez wielkości liter; proszę dodać opcję 
zmiany wielkości liter (2p).'''


def fun2():
    newList = glob.glob('*.py')
    for i in newList:
        print(i)
        with open(i, 'r') as p:
            for y, x in enumerate(p.readlines()):
                for slowo in x.split():
                    if slowo.lower() in keyword.kwlist:
                        print(str(y) + x)
                        break
# fun2()


##### ******************************************************************** #####
                                    # ZADANIE 3
##### ******************************************************************** #####
'''Proszę sporządzić histogram słów rozpoczynających się na daną literę alfabetu ze wszystkich 
plików z określonym rozszerzeniem w katalogu bieżącym, opcje wyświetlenia: sortowanie alfabetyczne
 bądź po częstościach (2p).'''
def fun3(typeOfFile,sortType):
    alfabet=list(map(lambda x: chr(x),range(97,123)))
    for fl in glob.glob('*.txt'):
        with open(fl) as pl:
            lines=pl.readlines()
            for i in lines:
                histogram = { }




##### ******************************************************************** #####
                                    # ZADANIE 4
##### ******************************************************************** #####
'''
Wszystkie pliki z rozszerzeniem in w katalogu bieżącym traktujemy jako wyniki kolejnych serii 
pomiarów tych samych wielkości. Zakładamy, że w każdym z plików mamy dwie kolumny liczb (x, y).
Na wyjściu chcemy otrzymać jeden plik z trzema kolumnami:
x pierwsza kolumna z dowolnego z plików wejściowych,
średnia y z danego wiersza ze wszystkich plików,
odchylenie standardowe y z danego wiersza ze wszystkich plików
PLIKI TESTOWE: pliki'''


def fun4():
    newDict = {}
    for plik in glob.glob('*.in'):
        with open(plik) as p:
            lines = p.readlines()
            for i in lines:
                newDict.setdefault(i.split()[0], []).append(float(i.split()[1]))
        with open("wynik.out", 'w') as wy:
            for k,w in newDict.items():
                wy.write(str(w[0])+" "+str(sum(w)/len(w))+" "+str(statistics.stdev(w))+"+\n")
#fun4()


##### ******************************************************************** #####
                                    # ZADANIE 5
##### ******************************************************************** #####
'''Proszę napisać funkcję, generującą plik z instrukcjami gnuplota pozwalający na wygenerowanie 
wykresu plików j.w. + wynikowego (łącznie z odchyleniem standardowym), proszę skorzystać z potrójnego cydzysłowu (2p).'''

def fun5():
    with open('gnu.sh', 'w') as fl:
        fl.write(
            '''
set term pdf
set out 'wykres.pdf'
plot '''
        )
        for i in glob.glob("*.in"):
            fl.write("'" + i + "' ")
        fl.write('wynik.out')

#fun5()

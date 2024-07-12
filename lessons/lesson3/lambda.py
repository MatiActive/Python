# wyrazenia lambda sa to jednolinijkowe anonimowe funkcje, bez nazwy. Tworzone sa za pomoca slowa lkluiczowego lambbda po ktorum nastepuje lista parametrow. Po dwukropku znajduje sie wlasciwy kod funkcji. Funkcje lmbda przyjmuje dwa argumenty a oraz b i zwraca ich sume return jnie jest potrzebne wynik wyrazenia jest automatycznie zwracany z lambda 

sum = lambda a,b: a+b 
print(sum(10,5))
print(sum(4,3))

print("--------------")
# wyrazenie lambda moze byc rowniez zwrocone przez zwykla funkcje dzieki czemu mozna ja wywolac w razie potrzeby 

def genFunc(n):
    return lambda a: a * n
doubler = genFunc(2) # w doubler jest lambda z n o wartosci 2

print(doubler(5))
print(doubler(7))
print(doubler(4))

tripler = genFunc(3)
print(tripler(5))
print(tripler(3))

# WyraZENIE lambda przydaja sie najbardziej w funkcjach wyzszego rzedy czyli takich, ktore jako argument przejmuja inne funkcje lub zwracaja funkcje 
# przykladem jest funkcja r = map(func, seq) przyjmuje funkcje ktora wywola na wszystkich elementach seq, po czym zwroci sekwencje zmodyfikowanych przez func elementow w postaci Iteratora, wiec mozna skonwertowac wynik na liste poprzez list()

listData = [1,2,3,4,5]

result = map(lambda x : x * 2, listData)
#map przechodzi po kazdym elemencie
print(list(result))

print(list(map(lambda x: x*3,[1,2,3,4])))

# funcka filter przyjmuje wyraenie lambdam ktore jesli zwroci true sprawi , ze dany element lizty znajdzie sie w wynikowej sekwencji 

listData = ["ola", "kola", "lasia","mateusz","tadeusz","wlodzimierz" ,"kasia"]

#filtruje uimiona, wybiera te ktore maja mniej niz 6 liter 
result = filter(lambda x: len(x) <= 5, listData)
print(list(result))

# funkcja reduce redukuje sekwencje do pojedynczej wartosci 
# musi byc zaimportowana 

from functools import reduce # import runkcji reduce

numSum = reduce ((lambda x, y : x + y), [1,2,3,4,5])
print("suma liczb", numSum)

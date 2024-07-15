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
print("-----")

# -----------------------------------------
#Lambda
# Funkcje lambda to anonimowe, krótkie funkcje jednowierszowe. Mogą być używane wszędzie tam, gdzie potrzebujesz funkcji, ale nie chcesz definiować jej za pomocą tradycyjnej konstrukcji def.

# Skladnia : lambda argumenty: wyrażenie
# Tradycyjna funkcja
def add(x, y):
    return x + y
# Lambda równoważna powyższej funkcji
add_lambda = lambda x, y: x + y
print(add(2, 3))  # Wyjście: 5
print(add_lambda(2, 3))  # Wyjście: 5

# Map
# map jest funkcją, która stosuje podaną funkcję do każdego elementu podanej sekwencji (np. listy) i zwraca iterator z wynikami.

# Składnia: map(function, iterable)
#Przykład:
numbers = [1, 2, 3, 4, 5]
squared = map(lambda x: x ** 2, numbers)
print(list(squared))  # Wyjście: [1, 4, 9, 16, 25]

# Filter
# filter jest funkcją, która stosuje podaną funkcję (zwracającą wartość logiczną) do każdego elementu sekwencji i zwraca iterator z elementami, dla których funkcja zwróciła wartość True.

#Składnia:filter(function, iterable)
#Przykład:
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
even_numbers = filter(lambda x: x % 2 == 0, numbers)
print(list(even_numbers))  # Wyjście: [2, 4, 6, 8, 10]
#Reduce reduce jest funkcją z modułu functools, która stosuje podaną funkcję do par elementów w sekwencji, zmniejszając sekwencję do pojedynczej wartości.

# Składnia: from functools import reduce 
# reduce(function, iterable)
#Przykład:
from functools import reduce
numbers = [1, 2, 3, 4, 5]
sum_of_numbers = reduce(lambda x, y: x + y, numbers)
print(sum_of_numbers)  # Wyjście: 15
#Podsumowanie
#Lambda: Umożliwia tworzenie krótkich, anonimowych funkcji.

#Map: Stosuje funkcję do każdego elementu iterowalnego obiektu i zwraca nowy iterowalny obiekt z wynikami.

#Filter: Filtruje elementy iterowalnego obiektu, zwracając tylko te, które spełniają podany warunek.

#Reduce: Redukuje iterowalny obiekt do pojedynczej wartości poprzez zastosowanie funkcji do par elementów.

# Oto kilka bardziej zaawansowanych przykładów użycia tych funkcji razem:
from functools import reduce
numbers = [1, 2, 3, 4, 5]
# Użycie map do podniesienia do kwadratu każdego elementu
squared = list(map(lambda x: x ** 2, numbers))
print(squared)  # Wyjście: [1, 4, 9, 16, 25]

# Użycie filter do wybrania tylko parzystych liczb
even_numbers = list(filter(lambda x: x % 2 == 0, squared))
print(even_numbers)  # Wyjście: [4, 16]

# Użycie reduce do zsumowania wszystkich elementów
sum_of_even_numbers = reduce(lambda x, y: x + y, even_numbers)
print(sum_of_even_numbers)  # Wyjście: 20

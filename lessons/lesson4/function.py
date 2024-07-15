# Przydatne funkcje z danymi - konwersje danych

# Podstawa pracy z danymi jest konwersja miedzy jednym typem a drugim np str na int

string = str(12.56)
print(type(string))

listData = str( [0,1,2,3] )
print( type(listData) )

number = int("67")
print(type(number))

number2 = float("20.03")
print(type(number2))

print("-----")
# FUNKCJE MATEMATYCZNE !!! 

import math
# wartosc bezwzgledna 

print(abs(5))
print(abs(-5))
# Zaokraglenie do najmniejszej liczby calkowitej nie mniej niz podana wartosc
print(math.ceil(6.78))
print(math.ceil(20.12))
print(math.ceil(-3.23))

# zaokraglenie do najwiekszej liczby calkowitej nie wiejszej niz podana wartosc 
print("-----")
print(math.floor(6.78))
print(math.floor(20.12))
print(math.floor(-3.23))
print("-----")
# max zwroci najwieksza wartosc z przekazanych
print(max(12,3,78,32,11))
print(max([9,67,43,-2])) 
print("-----")
#min zwroci najmniejsza wartosc z przekazanych
print(min(12,3,78,32,11))
print(min([9,67,43,-2]))
print("-----")

print(pow(2,3)) # to samo jak x**y = 8

print(math.sqrt(16)) # pierwiastek z 16 
#zaokraglenie do 3 miejsc po przecinku 
print(round(23.12345,3))
print("-----")
import random
# losowy float od 0 i mniejszy od 1 np 0.92
print(random.random())

# losowy element z listy, krotki lub str 
print(random.choice([4,3,8]))
print(random.choice(("ola", " ania", "adam")))

# losowy element z zakresu: start, stop, step
print(random.randrange(0,25,5))

# ustawia losowo elementy z listy 
listData = [0,1,2,3,4]
random.shuffle(listData)
print(listData)
#losowy float wiekszy od x i mniejszy od y  


print(random.uniform(2.3 , 10.78))

#dodatkowo python oferuje wiele funkcji trygonometrycznych jak acos(), asin(), atan(), cos(),
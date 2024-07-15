import math
import random
distance = int(random.uniform(100, 1000))
print("do punktu docelowego jest  "+str(distance)+ "km")

oil = (distance / 100) * 7
print("ilosc paliwa potrzebna na przebycie "+ str(distance)+"km : " + str(math.ceil(oil))+ "l")

oilPrice = round(random.uniform(4.5 , 5.5),2)
print("cela paliwa za litr: " + str(oilPrice)+ "zl")

cash = oil * oilPrice
cash = round(cash,2)
print("koszt podrozy wynosi: "+ str(cash)+ "zl")

if cash > 400:
    print("koszty podrozy sa wysokie")
else:
    print("koszty podrozy sa przystepne")
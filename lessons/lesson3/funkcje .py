# Definicje funkcji 
# funkcja to blok kodu, ktory moze byc wielokrotnie wywolany aby wykonac okreslona akcje. Funkcje sa podstawa programowania w kazzdym jezyku, gdyz udostepniaja wiele gotowych rozwiazan np print() do wyswietlania ingormacji w terminalu 
# funkcja definiuje sie slowem kluczowym def po ktorym nastepuje nazwa funkcji oraz nawiasy okragle wewnatrz ktorych moga byc parametry przekazane do funkcji zdefiniowane po przecinku. Nazwy tych zmiennych moga byc dozwolone, ale zgodnie z wymaganiami Pythona. Blok kodu funkcji rozpoczyna sie dwukropkiem, wymaga rozwniez wciecia . Funkcja moze zwrocic wartosc za pomoca slowa kliuczowego return.
# Wywolanie funkcji wykonuje sie za pomoca jej nazwy oraz nawiasow okragluch, przekazujemu rowniez wewnatrz nawiasow liste parametrow 

a = 2 
b = 4

def addNumbers(num1, num2):
    result = num1 + num2
    return result
c = addNumbers ( a , b)
print(c) # 6

d = addNumbers (c , 10)
print(d) # 16


# dla funkcji calcBasketValue wyciagany jest wartosc kazdego klucza z listy i sumowany w basketSum
def calcBasketValue(basketList):
    basketSum = 0
    for key in basketList:
        basketSum += basketList[key]
    return basketSum
shoppingBasket ={
    "smartphone" : 1200,
    "TV" : 1500,
    "console" : 1500
}
print(calcBasketValue(shoppingBasket))

# definiowanie funkcji -return

# Return na koncu funkcji jest oopcjonalne, umozliwia wyjscie z funkcji w dowolnym momencie 

def printList(listData):
    if len(listData) <= 3:
        #funkcjia konczy dzialanie jesli lista  ma mniej niz 3 lelementy 
        return
    print(listData)
    #return na koncu jest opcjonalne jesli nie zwraca jest konkretna wartowsc
    return
printList(["a","b","c"])
printList(["a","b","c","d","e"])

# Funkcja printList sprawdza czy przekazana lista ma mniej lub rowne 3 elementy, jesli tak to nastepuje wyjscie z funcji. Gdy jest 4 czy wiecej elementow zostaja wyswietlone w terminalu. Tlko drugie wywolanie funkcji pokaze liste
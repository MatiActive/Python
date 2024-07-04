
def displayShoppingList(shoppingList):
    print("Twoja lista zakupow: ")
    for item in shoppingList:
        print(" - ", item)

shoppingList = []

while True:
    product = input("podaj produkt lub koniec jesli chcesz wyjsc: ")
    if product == "koniec": break
    shoppingList.append(product)

displayShoppingList(shoppingList)
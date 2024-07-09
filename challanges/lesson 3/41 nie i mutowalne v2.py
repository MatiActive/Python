def calculateFinalPrice (initialPrice, discount):
    finalPrice = float(initialPrice) * (float(f"1.{discount}"))
    return finalPrice

reset = True
while True:
    if reset == True:
        initialPrice = input("podaj cene ktorej chcesz obliczyc rabat lub exit aby wyjsc : ")
        reset = False
        if initialPrice.lower() == "exit" : break
    discount = input("podaj procety rabatu pamietajac ze do 10 % musisz wpisac napierw 0 no 2% to 02 lub exit aby wyjsc: ")
    if discount.lower() == "exit" : break
    print("cena po rabacie: " + str(int(calculateFinalPrice(initialPrice, discount))) + str("zl") )
    reset = True
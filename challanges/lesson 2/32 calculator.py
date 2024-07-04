num = 0 
operation = None
reset = True
result = None
calcOperation = ["+" , "-", "*", "/", "**"]

while True:
    if reset == True:
        num = int(input("podaj pierwsza liczbe:"))
        reset = False
    operation = input("podaj znak operacji wybierajac z " + str(operation) + "mozesz wyjsc piszac exit lub reset : ")
    if operation == "exit" : break
    if operation == "reset":
        reset = True
        continue

    if not operation in calcOperation:
        reset = True
    
    secondNum = int(input("podaj druga liczbe :"))

    if operation == "+":
        result = num + secondNum
    if operation == "-":
        result = num - secondNum
    if operation == "*":
        result = num * secondNum
    if operation == "/":
        result = num / secondNum
    if operation == "**":
        result = num ** secondNum

    print("wynik dzialania "+ " " + str(num) + " " + "+" + str(secondNum) + " " + "=" + str(result))

    num = result
    result = None
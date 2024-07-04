print("zadanie 1")
number = 15 
if number > 15:
    print(str(number) + "jest wieksze 15")
elif number == 15:
    print(str(number) + "jest rowne 15")
    if number < 25:
        print("drugi warunek spelniony")
elif number == 20:
    print(str(number) + "jest rowne 20")
elif number == 25:
    print(str(number) + "jest rowne 25")
elif number > 30:
    print(str(number) + "jest wieksze od 30")
else:
    print("zadne nie spelnia warunkow")

print("--zadanie 2 --")


age = int(input("podaj swoj wiek : "))
weight = int(input("podaj swoja wage : "))

if age >= 18:
    if weight >= 50:
        print("spenia obydwa warunki")
    else:
        print("nie spelnia 2 warunku jestes za lekki")
else:
    print("jestes za mlody")
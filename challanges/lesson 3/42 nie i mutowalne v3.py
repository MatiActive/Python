def calculateBMI(weight, height):
    calBMI = weight / ((height / 100) ** 2)
    return calBMI

def classifyBMI(BMI):
    if BMI < 18.5:
        return "masz niedowage"
    elif BMI >= 30:
        return "Masz nadwage "
    else:
        return "Twoja waga jest git"

weight = int(input("podaj swoja wage: "))
height = int(input("podaj swoja wysokosc: "))

BMI = int(calculateBMI(weight, height))
print(BMI)
print((classifyBMI(BMI)))

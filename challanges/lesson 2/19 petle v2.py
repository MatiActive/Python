experience = 2

languages = ("python", "typescript", "javascript", "java")

contractType = "b2b"

if experience >= 2 and "python" in languages and "java" in languages:
    if contractType == "b2b" or contractType == "employment":
        print("warunki kandydata spelnione do zatrudnienia")
    else:
        print("nie spelnione warunki typu zatrudnienia")
else:
    print("warunki nie sa spelnione")

print("---kolejne zadanie----")

dogAge = int(input("podaj wiek swojego psa : "))

if dogAge == 1:
    humanAge = dogAge * 15
    print("wiek psa to :", humanAge)
elif dogAge == 2:
    humanAge = 15 + (dogAge -1) * 9
    print("wiek psa to :", humanAge)
elif dogAge > 2:
    humanAge = 24 + (dogAge - 2) * 5
    print("wiek psa to :", humanAge)
else:
    print("bledny wiek psa")


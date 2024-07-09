def calculateHumanYears(age):
        if age <= 2:
            return age * 10.5
        else:
            return 21 +(age - 2 ) * 4
            
while True:
    dogAge = float(input("wprowadz wiek spa w latach: "))
    humanYear = calculateHumanYears(dogAge)
    print("wiek psa w latach ludzkich: ", humanYear)
    again = input("czy chcesz obliczyc wiek innego psa? (TAK/NIE): ")
    if again.upper() != "TAK": break
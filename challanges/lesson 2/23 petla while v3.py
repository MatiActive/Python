iElements = int(input("podaj liczbe elementow do obliczenia : "))

sum = 0


if iElements > 0:
    i = iElements
    
    while i>0:
        i -= 1 

        num = float(input("podaj wartosc : "))
        sum += num
    sr = sum / iElements
    print("srednia", sr)
else:
    print("nie mozna obliczyc sredniej")
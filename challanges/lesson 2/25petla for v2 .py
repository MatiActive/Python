numberList = {-4,-3,-2,-1,0,1,2,3,4}

for i in numberList:
    if i == 0:
        print("zero jest parzyste", i)
    elif i % 2 == 0:
        print("liczba parzysta", i)
    else:
        print("liczby nieparzyste", i)
list = [1,2,3,4,5,6,7,8,9,10]

for i in list:
    if i % 2 == 0:
        continue
    elif i > 8:
        break
    else:
        print("liczba : ", i ** 2)


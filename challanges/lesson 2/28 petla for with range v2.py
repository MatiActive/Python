n = int(input("podaj liczbe "))
list=[]

for i in range(1,n + 1):
    list.append(i ** 2)
if list:
    print(list)
else:
    print("lista jest pusta")
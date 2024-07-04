text = ("hello")
print(text.upper())
print(dir(text))

x = 256
y = 256
print(x is y)

listOne = [1,2,3,4,5]
listTwo = listOne
print(listOne is listTwo)

listOne.append(6)
print(listOne)
if listOne is listTwo:
    print("nic sie nie zmienilo")
listThree = [1,2,3,4,5]
print("-------")
if listThree is listOne:
    print("jest takie same")
else:
    print("nie jest takie samo")
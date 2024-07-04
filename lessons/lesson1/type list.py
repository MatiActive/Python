lista1 = ["mateusz","sylwia","wojtek","bartek","rafal"]
print(lista1)
print(len(lista1))
print(lista1[2]) # trzecia osoba z listy 
print(lista1[0]) #pierwza osoba z luisty

print(lista1[-1]) # ostatnia osoba 
print(lista1[-3]) #pierwsza osoba 

print(lista1[2:4])
print(lista1[2:])
print(lista1[::2])

lista1[2] = "Kajtek"
print(lista1)
del lista1[3]
print(lista1)
print("sylwia" in lista1)
print("wojtek" in lista1)
if "rafal" in lista1:
    print("siemano kolano")
print("------")
for i in lista1:
    print(i)
print("------")
data = [
    ["pawel", "wojtek"],
    ["jacek", "andrzej", "roman", "kamil"],
    ["darek", "michal"]
    ]
print(data)
print(len(data))
print(len(data[1]))
print(data[0])
print(data[2])
print(data[0][1])


tab1 = [1,2,3]
tab2 = [4,5,6]
numbers = tab1 + tab2 
print(numbers)

mutliNumbers = numbers * 3
print(mutliNumbers) 
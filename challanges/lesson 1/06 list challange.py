data = [ 0, 1, 2, 3, 4, 5, 6]
print(len(data))
del data[2]
del data[3]
print(len(data))
print(data)
if 3 in data:
    print("liczba 3 jest w zbiorze")

for i in data:
    print(i)
print("---")
for i in data:
    print(i*2)
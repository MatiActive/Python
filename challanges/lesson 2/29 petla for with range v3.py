n = int(input("podaj liczbe"))

parzyste = []

nieparzyste = []

for i in range(1, n + 1):
    if i % 2 == 0:
        parzyste.append(i)
    else:
        nieparzyste.append(i)
print(parzyste)
print(nieparzyste)
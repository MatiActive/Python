numbers = [7, 8, 9, 10, 11, 12]

print(numbers) 

tuplesNumer = tuple(numbers)
print(tuplesNumer)

mixedList = ["Ola", 12, 13.2]
print(mixedList)

setMixet = set(mixedList)
print(type(setMixet), setMixet)

frozenSetNumbers = frozenset(tuplesNumer)
print(type(frozenSetNumbers), frozenSetNumbers)

nameAgePairs = (("ola", 19), ("marek", 24))
ageDict = dict(nameAgePairs)
print(ageDict)
print(ageDict["marek"])

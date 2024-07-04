setData = {1,3,5,7,12,38}
print("-----wydruk lancucha set z jego typem-----")
print(setData)
print(type(setData))
print("----Dodanie liczby 22 do zbioru + wydruk -----")
setData.add(22)
print(setData)
print("-----usuwanie liczby 5 i wydruk-----")
setData.discard(5)
print(setData)
print("----Iteracja zbioru-----")

for i in setData:
    print(i)
print("-----zmiana zbioru na niezmienialny frozenset----")
frozenSet = frozenset(setData)
print("-----wydruk lancucha frozenset z jego typem-----")
print(frozenSet)
print(type(frozenSet))
#print("-----proba dodania liczby 24-----")
#frozenSet.add(24) nie bedzie dzialac gdyz jest niezmienialny
print("----Iteracja zbioru-----")

for i in frozenSet:
    print(i)
a = 1 
addr1 = id(a)
print(addr1)

a += 1 # zwiekszenie o 1 

addr2= id(a)
print(addr2)

# float, bool str, int , tuple, frozenset sa wartosciami niemutowalnymi co oznacza za to po zmianie to nie jest ta sama liczba tylko nowa wartosc w pamieci co  wskazuje inne id nie mozna zmienic ich wartosci w pamieci 

#mutable list set i dict
listData = ['a', 'b']
adrr1 = id(listData)
listData += ['c', 'd']
adrr2 = id(listData)
print("sa takie same w sicie bo jest mutowalna", addr1, addr2)

setData = {5,6}
aadr1 = id(setData)
setData.add(7)
print(setData)
aadr2 = id(setData)

print("zbior tez jest mutowalny ", aadr1, aadr2)

dictData={"a" : 0, "b" : 1 }
ddr= id(dictData)
dictData["c"] = 2
print(dictData)
ddr2 = id(dictData)
print("tez sa takie same ", ddr,ddr2) 


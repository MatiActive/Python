# przakazanie wwartosci do funkcji w postaci aprametrow utowalne i niemutowalne

# Definiujac funkcje oraz przyjmowanie przez nia parametry musimty pamietac o charakterystyce typow w python. Typy niemutowalne int, float, tuple, str i bool czyli ich zmiana tworzy nowy element w pamieci. Typy mutowalne przy modyfikacji nioe tworza nowego elementu w pamieci, sa mienne np. set, list, dict

f = 3.2 
addr1 = id(f)

f = f+ 2.5 
addr2 = id(f)

print(addr1)
print(addr2)
print(addr1 == addr2)

listData = ['a', 'b']
addr1 =id(listData)
listData += ['c', 'c']
addr2 =id(listData)

print(addr1)
print(addr2)
print(addr1 == addr2)


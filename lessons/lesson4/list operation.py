# Praca z listami 

list1 = [0,1,2,3,4,5,6]

print(list1[2]) # pobranie elementu : 2
print(list1[2:4]) # pobranie zakresu: [2,3] 

list2 = ["ania", "ola", "rafal", "adam"]
list2[2] = "daniel" # zmiana elementu 
print(list2) # ['ania', 'ola', 'daniel', 'adam']

del list2[1] # skasowanie elementu 
print(list2) # ['ania', 'daniel', 'adam']

print( len(list2)) # dlugosc listy : 3
print( max([4,8,1])) # 8
print(min([4,8,1])) # 1
# zmiana krotki na liste 
print( list( (10,20) ) )# [10,20]
# operatory i listy 

print( [0,1] + [2,3]) # laczenie [0, 1, 2, 3]

print( [3,2] * 2) # powtorzenie [3, 2, 3, 2]

print( 5 in [3,4,5]) # True 
print( 0 not in [3,4,5]) # True
print( 2 not in [2,3,4,5]) # False

list3 = ["ola", "ania", "adam"]

for x in list3:
    print(x)

list4 = ["ania","basia" ,"ola"]
list4.append("ola")
print(list4) #['ania', 'basia', 'ola', 'ola']

# ilosc powtorzen 
print(list4.count("ola")) # 2

# dodanie elementow do listy z ionnej sekwencji 
list4.extend(["rafal", "kasia"])
print(list4) # ['ania', 'basia', 'ola', 'ola', 'rafal', 'kasia']

print(list4.index("ola")) # zwraca najmniejszy index wystapienia wartosci, 2

# umieszczenie elementu pod indeksem, przesuwa istniejace dalej
list4.insert(0,"kinga")
print(list4) # ['kinga', 'ania', 'basia', 'ola', 'ola', 'rafal', 'kasia']

list5 = [6,0,1,2] 
list5.reverse() # odwrocenie kolejnosci
print(list5) # [2, 1, 0, 6]

list5.sort() # sortowanie
print(list5) # [0, 1, 2, 6]
# zwraca i zabiera ostatni element z listy 
print(list5.pop()) # 6
print(list5) # [0, 1, 2]
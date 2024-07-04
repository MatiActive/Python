# krotki sa podobne do listy ale jest niezmienialna 

ludziki = ("ania", "bania", "kania" )

print(ludziki)
print("typ danych ludziki : ", type(ludziki))

print("---")

#ludziki[1] = dran nie zadziala bo jest nie zmienialny 
#del ludziki[0] # blad potwierdza ze sa niezmienialne 
#ale mozna dodac przy tworzeniu nowej zmiennej 

ludzikiPlus = ludziki + ("duren",) # jesli jest jeden argument to musi byc przecinek   
print(ludzikiPlus)

print("---")
print(ludziki[1]) # tak samo mozna wywolac jedna wartosc 
print(ludziki[-1]) # i odwrotnie 

ludzikiv2 = tuple( ("jak", "tak", "brak") )
print(ludzikiv2) # inny sposob tworzenia 
print(type(ludzikiv2))

print(ludzikiv2 * 2)
print(len(ludzikiv2))

#identycznier jak w listach funkcja i in 

if "duren" in ludzikiPlus:
    print("duren jest tutaj ")

# petla tez dziala 

for i in ludzikiPlus :
    print(i)

#krotka w krotce 

card = (("AS", "jopek","queen"),("krol"))
print(card)
print(type(card))
print(len(card))
print(len(card[0]))
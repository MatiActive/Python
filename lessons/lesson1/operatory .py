print("------Operatory arytmetyczne------")
a = 20 
b = 3 
result = a + b ; print(result) # dodawanie 
result = a - b ;  print(result) # odejmowanie
result = a * b ; print(result) # mnozenie
result = a / b ; print(result) # dzielenie zawsze zwraca wartosc zmiennoprzecinkowa 3.0
result = a % b ; print(result) # reszta z dzielenia 
result = a ** b ; print(result) # potegowanie
result = a // b ; print(result) # dzielenie dajace tylko liczbe calkowita 

print("----Operatory przypisania----")

a = 10  # operator przypisania wartosci do zmiennej 

a += 2 ; print(a)# to samo co a = a + 2 
a -= 1 ; print(a)# to samo co a = a - 1 
a *= 3 ; print(a)# to samo co a = a * 3 
a %= 10 ; print(a)# to samo co a = a % 10 
a **= 3 ; print(a)# to samo co a = a ** 3 
a //= 10 ; print(a)# to samo co a = a // 10 
print("--------operatory porownania--------")
# wsztstkie operatory maja wynik boolean czyli true i false 
result = 10 == 8
print(result)
print(10 == 10)# czy 10 jest rowne 10 
print(10 != 8) # czy 10 nie jest rowne 8 
print(4 > 1) #czy 4 jest wieksze od 1 
print(4 > 10) #czy 4 jest wieksze od 10 
print(3 < 5) # czy 3 jest mniejsze od 5 
print(12 >= 10) # czy 12 jest wieksze badz rowne 10  
print(11 <= 10) # czy 11 jest  mniejsze badz rowne 10 

if 10 > 11:
    print("10 jest wieksze")
else:
    print("jest mniejsze")

print("-----Operatory logiczne -------")

# operatpry logiczne umozliwiaja laczenie wielu porownan aby uzyskac jedna ostateczna wartosc logiczna true lub false zwykle stosowane sa w instrukcjach i w petlach 
# operator and zwraca wartosc true jewsli obie strony wyrazanie maja wartosc true


print( True and True ) # zwraca true
print( True and False ) # zwraca false
print( False and False ) # zwraca true
print("-----")
print( 8 > 3 and 3 == 3) 
print( 4 >= 4 and 1 >= 10)
print( 10 ==5 and 3 < 1)
print("-----")
#operator or zwraca wartosc Trule jesli przynajmniej jedna ze stron zwroci True, czyli or zwroci false jesli obie strony maja False 

print( True or True) # true
print( True or False) # true
print( False or False) # false
print("-----")
print( 10 > 1 or 7==7 )
print( 10 >= 5 or 7 < 12)
print(10 == 11 or 2 > 3)

if "ania" == "ania" or 10 == 1:
    print("ania to ania")
print("-------")
# operator not odwraca wartosc logiczna i jesli byla tru jest false i odwrotnie 

print(not True) # false
print(not False) # true 

print( not  ( 10 == 10)) # false
print (not (10<12) ) # true
print(not (10>5 and 12<14) ) # false 

taskComplited = False

if not taskComplited:
    print("zadanie nie zostalo ")
else:
    print("zostalo wykonane")
#wytlumaczenie ifa taskComplited ma wartosc False dlatego przy uzyciu not zmienia wartosc logiczna wyrazenia na true czyli if zostaje wykonany
print("-----Operatory przynaleznosci------")


#operatory przynaleznosci in i not in pozwalaja na okreslenie czy dana wartosc jest w sekwencji danych false jesli jej nie ma

date = [1,2,3,4,5,6]
print( 0 in date)
print( 5 in date)
print("ola" in ("ania", "ola", "kasia"))

print(12 not in date)
print(2 not in date)
print("----operatory tozsamosci-----")


# operatory tozsamosci is i is not porownuja lokalizacje w pamieci operandow w przypadku is jesli operandy wskazuja na to smamo miejsce w pamieci to zwrocone jest true w przypadku is not na odwrot zwroci true jesli nie wskazuja na to samo miejsce w pamieci 

a = [1,2,3,4,5]
b = [1,2,3,4,5]
c = a

print(a is b)
print(a is a)
print(b is b)
print(a is c)
# a is c daje wartosc true gdyz wskazuja na to samo miejsce w pamieci a mimo ze b ma takie same wartosci to nie wskazuja na te same miejsce 
print(a is not c)
print (a is not b)
print(a is not a)

print("----operator konkatenacji-------")

#sluzy do laczenia lancuchow znakow list i zbiorow 


znak= "hello"
znak2= znak + "world"
print(znak2)

list1 = [1,2,3,4]

listData = list1 + [5,6]
print(listData)

tuple1 = ("one", "two")
tuple2 = ("three",)
print(tuple1 + tuple2)


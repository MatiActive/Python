# Formatowanie ciagow tekstowych w pythonie umozliwia wstawianie wartosci zmiennych bezposrednio do tekstow, co ulatwia tworzenie dynamicznych wiadomosci i ratortow. or werscji python 3.6 dostepna jest wygodna metoda formatowanie ciagow znakow znana jako f-string (formatted string literals).

# podstawy f-string 
# aby uyc f-string, wystarczy popredzic ciag znakow litera f lub F przez otwarciem cudzyslowu. Wewnatrz ciagu znakow w nawiasach klamrowych mozna umieszczac wyrazenia ktore zostana zastapione ich wartosciami 

wiek = 27 
# wczesniej napisalbym tak : 
print("aktualny wiek", wiek, "lat")
# ale to lepiej wygladjacy kod 
print(f"aktualny wiek {wiek} lat")

pi = 3.141592
print(F"warotsc liczby pi to doklanie {pi:.2f}")#warotsc liczby pi to doklanie 3.14

list = ["ananas", "cytryna"]
print(f"lista zazkupow: {list}")#lista zazkupow: ['ananas', 'cytryna']

person = {"name" : "Mateusz",  "age" : "27"}
print(f"User: {person}, {person['name']}")

a =5 
b = 10 
print(f"wynik dodawanie liczb {a} i {b} to dokladnie : {a + b}")

score = 55 
print(f" Test zakonczony {('sukcesem' if score >= 70 else 'porazka') }")
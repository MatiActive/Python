class Person:
    def __init__(self, name, surname, country):
        self.name = name
        self.surname = surname
        self.country = country

    def getFullName(self):
        return self.name + " " + self.surname
    def printData(self):
        print(self.name, self.surname, self.country)

person1 = Person("Ola", "Kowalska", "Polska")
print("Full name ", person1.getFullName())

person1.printData()

# w klasie moze byc zzdefiniowana specjalna metoda tzw konstruktor o nzawie __init__ bedzie wywolana podczas tworzenia instacji obiektu np:
# person2 = Person("Ala", "Test", "UK") 
# Konstruktor zwykle stosuje sie do zainicjowania zmiennych wewnatrz klasy wartosciami z argumentow przekazzanych do konstruktora oraz innymi potrzebnymi operacjami

# Uwaga: Kazda metoda w klasie, w tym konstruktor zawsze przyjmuje obowiazkowy pierwszy argument self, ktory wskazuje na aktualny obiekt na ktorym operujemy podczas wywolywania metody/konstruktora. Dzieki self moznemy zmienic wartosci zmiennych w obiekcie oraz wwywolac inne metody. 

class Book:
    def __init__(self, author, title, isbn, year):
        self.author = author
        self.title = title
        self.isbn = isbn
        self.year = year 

    def getFullBookName(self):
        print(self.author, self.title, self.isbn, self.year)

book1 = Book("Adam Mickiewicz", "Pan Tadeusz", "5434Xas", "1860" )

book1.getFullBookName()
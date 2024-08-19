class Employee:
    #statyczna, wspolna zmienna dla wszystkich obiektow 
    # na bazie klasy employee 
    numEmployees = 0

    def __init__(self, name):
        self.name = name # atrybut obiektu 
        print("self.name : ", self.name )

        # zwiekszenie wartosci wspolnej statycznej zmiennej 
        Employee.numEmployees +=  1
        print("Employee.numEmployees", Employee.numEmployees)

employee1 = Employee("Ola")
employee1 = Employee("Asia")
employee1 = Employee("Kasia")

print("number of employees: ", Employee.numEmployees)
# Zmienna statyczna tworzymy wewnatrz klasy, poza konstruktorem i metoda.
# Ciekawa wlasciwoscia takiej statycznej zmiennej jest fakt ze jest tylko jedna i jedna dla wszystkich instancji obiektu na bazie danej klasy.
# W przykladzie zmienna statyczna jest numEmployees zdefiniowana na poziomie klasy. Dostep do niej uzyskuje sie przez nazwe klasy i nazwe zmiennej statycznej 

class Employee: 
    "Employee class describing company employee"
    # static variables for all objects based on Employee
    numEmployees = 0
    employeesList = []

    def __init__(self, name):
        "Constructor for Employee"
        """
            line 1
            line 2
        """
        self.name = name

        Employee.numEmployees += 1
        print(self.name, "numEmployees: ", Employee.numEmployees)

        Employee.employeesList.append(self)

    
    def printAllEmployees(self):
        for el in Employee.employeesList:
            print(el.name)


employee1 = Employee("Ola")
employee2 = Employee("Kasia")
employee3 = Employee("Adam")
employee4 = Employee("Karol")

print("Employee.numEmployees: ", Employee.numEmployees)
print()

employee1.printAllEmployees()

print(Employee.__doc__)
print(Employee.__name__)
print(Employee.__module__)

print("name attr in Employee: ", hasattr(employee1, "name") )
print("city attr in Employee: ", hasattr(employee1, "city") )
employee1.city = "Krk"
print("city attr in Employee: ", hasattr(employee1, "city") )

setattr(employee1, "name", "Kasia")
print("employee1.name: ", getattr(employee1, "name") )
 
print("DOCK STRING DEFINICJA ")

class Person:
    'string do dokumentacji: klasa Person opisujaca osobe'
    
    def __init__(self, name, surname):
        print(Person.__name__)  # nazwa klasy
        self.name = name
        self.surname = surname
        self.printDocString()
        print(Person.__module__) # __main__ w trybie interaktywnym
    
    def printDocString(self):
        print(Person.__doc__)
    
    def manageAttributes(self):
        # Czy istnieje atrybut w obiekcie
        print(hasattr(self, "city"))  # False, ponieważ atrybut "city" nie istnieje
        print(hasattr(self, "name"))  # True, atrybut "name" istnieje

        # Pobranie wartości atrybutu
        print(getattr(self, "name"))  # Zwraca wartość atrybutu "name" (Ola)

        # Ustawienie nowego atrybutu
        setattr(self, "country", "Poland")
        print(self.country)  # Zwraca "Poland"

        # Skasowanie atrybutu
        delattr(self, "country")
        # print(self.country)  # To spowodowałoby błąd, ponieważ "country" zostało usunięte


# Tworzenie instancji obiektu Person
person1 = Person("Ola", "Kowalska")

# Wywołanie metody zarządzającej atrybutami
person1.manageAttributes()

# String dokumentujacy to lancuch znakow w pierwszej linijce definicji funkcji, metody czzy klasy. Moze byc pobrany za pomoca nazwy klasy oraz atrybutu__doc__

# Takie lancuchy stanowia opis dzialania danej funkcjonalnosci wiekszej czesci kodu np. klasy, modulu itd. Nie nalezy myslic tych informacji z komeentarzami, ktore opisuja konkretny kon np. jak dziala 

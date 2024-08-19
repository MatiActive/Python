class Dog:
    def __init__(self):
        print("Konstruktor!")

    def __del__(self):
        print("Destruktor!")


dog1 = Dog()

class Person: 
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        print("object created: " + self.getFullName())

    def getFullName(self):
        return self.name + " " + self.surname
    
    def __del__(self): # destruktor
        print("zniszczenie obiektu: " +self.getFullName())

person1 = Person("Ola", "Kowalska")
print(person1.name)
print(person1.surname)
print("Full name: ", person1.getFullName())
del person1 # zniszczenie obiektu i wywolanie destruktora

# Destruktor to specjalna metoda wywolywana kiedy niszczony jest obiekt za pomoca operatora del
# zanim obiekt bedzie skasowany z pamieci destruktor daje nam szanse na jeszcze jakies ostatnie operacje np. zamkniecie dostepu do plikow itp.

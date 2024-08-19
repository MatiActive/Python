# Programowanie obiektowe w Python - definicja klasy 
# Ponizej jest definicja klasy Car na ktorej podstawie powstana obiekty. Klasa to taki szablon co powolany obiekt ma zawierac np zmienne oraz metody. 

class Car:
    # konstruktor, specjalna metoda inicjujaca obiekt. jest wywolany podcas utworzenia instancji obiektu self to pierwszy parametr zawsze majacy obiekt na rzecz ktorego wywolana jest metoda 

    def __init__(self, brand, model, year):
        self.carName = brand + " " + model
        self.productionDate = year 

    # metoda printInfo otrzymuje tylko jeden obowiazkowy parametr self czyli obiekt na  ktorym jest wywolana metoda 

    def printInfo(self):
        print(self.carName + " " + str(self.productionDate))

    # klasa Car uzywana jest jako szablon do powolania dowolnej ilosci obiektow na jej podstawie ponizej dwa obiekty klasy Car 

mustang = Car("Ford", "Mustang", 1970)
mustang.printInfo()

viper = Car("Dodge", "Viper", 1997)
viper.printInfo()
print("przerwa".center(20,"*"))
class Person:
    def __init__(self, name, surname, job, experiencYear ):
        self.worker = name + " " + surname
        self.workExp =  job + " " + str(experiencYear)
        self.setAge(28)
        self.personExp()
    
    def personExp(self):
        print(self.worker + " " + self.workExp + " " + str(self.Age) )
    def setAge(self, newAge):
        self.Age = newAge
worker1 = Person("Wojtek", "Osmanski", "Libro", 10 )
worker2 = Person("Bartosz", "Rogowicz", "Ksiadz", 2 )
worker2.setAge(27)
worker2.personExp()
#worker1.workExp = "28"
#worker1.personExp()

print("przerwa".center(20,"*"))


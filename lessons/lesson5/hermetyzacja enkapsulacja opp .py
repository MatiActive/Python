class Person:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.__pesel = 34254434534
    def __getThePeselInfo(self):
        return "Pesel to " + str(self.__pesel)
    def printInfo(self):
        print(self.name, self.surname, self.__pesel)
person1 = Person("Yeti", "Kotleti")
#person1.__getThePeselInfo() # blad 
# print(person1._Person__getThePeselInfo()) mozna wejsc ale nie jest zalecane
person1.printInfo()
#print(person1.__pesel) # Blad

class Zlodziej(Person):
    def __init__(self, name, surname):
        Person.__init__(self,name, surname)
        #print(self.__getThePeselInfo()) # blad attribute error
        print(self.printInfo())
zlodiejaszek  = Zlodziej("YeeTi", "Kotleti")

print("Gettery i settery".center(50,"_"))

class Vw:
    def __init__(self):
        pass

    @property
    def gear(self): # getter pobiera wartosc
        print("getter : ", self.__gear)
        if(self.__gear > 3):
            return self.__gear
        else:
            return -1 
        
    @gear.setter # setter ustawia wartosc 
    def gear(self, newGear):
        print("newGear: ", newGear)
        if(newGear > 0): self.__gear = newGear

sm = Vw()
sm.gear = 2
print(sm.gear)
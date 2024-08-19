class Person: 
    def __init__(self, name, surname, city):
        self.name = name
        self.surname = surname
        self.city = city 
        print("Person Constructor")

    def printPersonData(self):
        print("Person : ", self.name, self.surname, self.city)
person1 = Person("Mateusz", "Narkiewicz", "Ilw")
person1.printPersonData()
print("Next Constructor".center(30,"*"))

class Employee(Person):
    def __init__(self, name, surname, city, workplace, salary):
        Person.__init__(self,name, surname, city)
        self.workpace = workplace
        self.salary = salary
        print("Employee Constructor")
    def printEmployeeData(self):
        print("Employee : ", "Miejsce pracy : " ,self.workpace, "Zarobki :", self.salary)
employee1 = Employee("Mateusz", "Narkiewicz", "Ilw" ,"kolchoz", ":(")
employee1.printPersonData()
employee1.printEmployeeData()

class Menager(Employee):
    def __init__(self, name, surname, city, workplace, salary, menagerSalary):
        Employee.__init__(self,name, surname, city, workplace, salary)
        self.menagerSalary = menagerSalary
        print("Menager Construction")
    def printMenagerData(self):
        print("Menager benefit :  ", self.menagerSalary)
menager1 = Menager("Sylwia", "Sendyk", "Ilw", "Studio Figura", "w chuj ", "jeszcze wiecej")
menager1.printPersonData()
menager1.printEmployeeData()
menager1.printMenagerData()
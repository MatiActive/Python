# Zapis pliku binarnego z modulem pickle - zapis danych binarnych w postaci calych obiektow nazywamy serializacja, odczyt takich danych okresla sie mianem deserialiazcji

import os 
import pickle

script_dir = os.path.dirname(__file__)

myInt = 1997
myString = "Siemano Kolano"
myList = ["Mati","Yeti","Kotleti"]

# zapis w formanie binarnym 

fh = open(script_dir+ "/6.1 data.dat", "wb")

pickle.dump(myInt, fh)
pickle.dump(myList, fh)
pickle.dump(myString, fh)

fh.close()

fw = open(script_dir+ "/6.1 data.dat", "rb")

rok = pickle.load(fw)
rok2 = pickle.load(fw)
rok3 = pickle.load(fw)
fw.close()
print(rok)
print(rok2)
print(rok3)

# Zapis obiektu na bazie definiowanej klsy z pickle - serializowac mozna dowolne obiekty np na bazie klas naszego programu co umraszcza prace z danymi 

import os 
import pickle

class Person:
    def __init__(self, name, surname, city):
        self.name = name
        self.surname = surname
        self.city = city 

    def __str__(self):
        return str(self.name) + " " +  str(self.surname) + " " + str(self.city)

person1= Person("Adam", "Kot", "Krk")
person2 = Person("Ola", "Kowalska", "Waw")

people = [person1, person2]
fh = open(script_dir + "/6.2 persons.dat", "wb")
pickle.dump(people,fh)
fh.close()

fw = open(script_dir + "/6.2 persons.dat", "rb")

persons= pickle.load(fw)
fw.close()
print(persons)
for person in persons:
    print(person)

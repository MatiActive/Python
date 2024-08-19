# Zapis pliku binarnego z modulem pickle - zapis danych binarnych w postaci calych obiektow nazywamy serializacja, odczyt takich danych okresla sie mianem deserialiazcji

import os 
import pickle

script_dir = os.path.dirname(__file__)

myInt = 1997
myString = "Siemano Kolano"
myList = ["Mati","Yeti","Kotleti"]

# zapis w formanie binarnym 

fh = open(script_dir+ "/data.dat", "wb")

pickle.dump(myInt, fh)
pickle.dump(myList, fh)
pickle.dump(myString, fh)

fh.close()

fw = open(script_dir+ "/data.dat", "rb")

rok = pickle.load(fw)
rok2 = pickle.load(fw)
rok3 = pickle.load(fw)
fw.close()
print(rok)
print(rok2)
print(rok3)

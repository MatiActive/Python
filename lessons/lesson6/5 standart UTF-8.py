# Zapis pliku z kodowaniem UTF -8 - praca z polskimi ogonkami czy innymi specyficznymi znakami wymaga skorzystania z kodowania znakow w standardzie UTF-8, dzieki temu unikniemy dziwacznych symboli przy probie zapisu takich znakow.

import os 
script_dir = os.path.dirname(__file__)
print("skrypt znajduje sie w : ", script_dir)

fh = open(script_dir + "/5.1 ogonki.txt", "w", encoding="utf-8")
fh.write("Polskie ogonki ąśćńłę. \n")
fh.write("kolejne ogonki ęńćśął. \n")
fh.close()

# odczyt pliku z kodowaniem utf-8 praca z polskimi ogonkami czy innymi specyficznymi znakami wymaga skorzstania z kodowania znakow w standardzie utf-8. dzieki temu unikniemy dziwacznych syumboli przy probie zapisu takich znakow 

import os 
fh = open(script_dir + "/5.1 ogonki.txt", "r", encoding="utf-8")
#lines = fh.readlines() # odczyt wszystkich lini
#fh.close()

#for line in lines:
#    print(line)

while True:
    line = fh.readline()
    if not line:
        break
    print(line)
fh.close()
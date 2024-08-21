# DODATKOWE INFORMACJE O PLIKU - MODUL OS ZAPEWNIA WIELE PRZYDATNYCH FUNKCJI DO OPERACJI NA PLIKACH
import os
import shutil

script_dir = os.path.dirname(__file__)

fh = open(script_dir + "/7.1 data.txt", "w", encoding="utf-8")
fh.write("Polskie ogonki ąśćńłę.\n")
fh.close()
if not os.path.exists(script_dir + "/7.1 newdata.txt"):
    os.rename(script_dir + "/7.1 data.txt", script_dir + "/7.1 newData.txt")
        # zmiana nazwy pliku ^
print(os.path.getsize(script_dir+"/7.1 newData.txt")) # wielkość pliku "29" 
print("File exists", os.path.exists(script_dir + "/7.1 newData.txt")) # czy isnieje "File exist True"
print("isfile", os.path.isfile(script_dir + "/7.1 newData.txt"))#isfile True
print("isdir", os.path.isdir(script_dir + "/7.1 newData.txt"))# isdir False

if not os.path.exists(script_dir + "/subDir"):
    os.mkdir(script_dir + "/subDir") # utworzenie nowego katalogu
    os.rmdir(script_dir + "/subDir") # skasowanie katalogu

os.remove(script_dir + "/7.1 newData.txt") # skasowanie pliku
#os.chdir(script_dir) # ustawienie bieżacego folderu - current working dir
#if not os.path.exists(script_dir + "/data-copy.dat"):
#    shutil.copyfile(script_dir + "/6.1 data.dat", script_dir + "/data-copy.dat")
#    #kopiowanie 6
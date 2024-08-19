# Obsługa pliów - odczyt plikow to podstawowa umiejetnosc kazdego programisty . Pliki konfiguracyjne, tekstowe czy bardziej zaawansowane bazy danych pozwalaja na przechowanie danych dla naszych programow.

# Aby otworzyc plik trzeba uzuc metodę open, przekazać scieżke do pliku oraz trybu otwarcia pliku, fuknkcja zwraca uchwyt do pliku na bazie, ktorego mozna wykonywać rożne operacje.

fh = open("test.txt", "w") # plik test.txt odtarty do zapisu
fh.write("content1\n") # zapis tresci "content" do pliku 
fh.write("content2\n")
fh.close() # zakończenie pracy z plikiem 

# Tryby otwarcia pliku:
#  r - otwarcie pliku tylko do odczytu
# rb - odczyt pliku w formacie binarnym'
# w - plik otwarty do zapisu, zanim bedzie zapis na początku tresc pliku  jest usuwana
# a - otwarcie pliku do zapisu, dodanie tresci na koniec pliku, czyli tresc nie jest kasowana Dodanie + powoduje otwarcie pliku zarowno do odczytu i zapisu np. r+(odczyt i zapis)

fh2 = open("test.txt", "a")
fh2.write("content3\n")
fh2.close()

print("NEXT".center(16, "-"))

# Obsluga plikow - scieżki plikow moga byc relatywne lub absolutne 1
# scieżka wzgledna inaczej zwana relatywna wskazuje na plik lub folder w aktualnej lokalizacji np. wzgledem folderu gdzie aktualnie wykonywany jest skrypt Pythona.
# Ścieżka absolutna to pelny adres do pliku np: c:\Users|mati...

# Poniższy program tworzy plik file1.txt, czyli uzywajac scieżki wzglednej/relatywnej.
# gdzie pojawi sie plik ? w tym samym folderze co program czyli w katalogu lesson6


# program python/lesson06/ relative_path.py

try:
    fh = open("file1.txt", "w")
    fh.write("content") # content pliku
    fh.close() # zakonczenie pracy z plikiem
except:
    print("IOError occured")


# Ścieżki plikow - Plik file1.txt pojawił sie w aktualnym folderze na ktorym wykonuje sie srypt Pythona tzw. current working directory czyli /home/matiactive/python_lessons 
print("NEXT".center(16, "-"))

import os 

print("path to script __file__:", __file__) # absolutna scieżka do skryptu
script_dir = os.path.dirname(__file__) # absolutna ścieżka do katalogu skryptu
print("script located in folder, script_dir:", script_dir)
# ścieżka absolutna na ktorym katalogu skrypt jest wykonywany
print("current working directory: os.getcwd", os.getcwd())


print("NEXT".center(16, "-"))
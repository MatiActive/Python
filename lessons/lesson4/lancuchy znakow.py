print("hello" + "world") # konkatenacja helloworld
print("hello" * 2) # powtorzenie hellohello

string = "hello"
print(string[1]) # e
print( string[1:3]) #zakres: el 
print("o" in string) # True
print("x" not in string) # True

multiLine = """line1
line2
""" # tekst w wielu liniach
print(multiLine) 

print("some text".capitalize()) # Some text 
print("ok ok ok".count("ok")) # zlicza ilosc ok : 3

# wycentrowanie tekstu do 10 znakow z * 
# ***tekst***
print("tekst".center(11,"*"))
print("hello world".endswith("world"))# True
print("Hello world".startswith("Hi")) #False nie zaczyna sie na Hi

# wyszukuje lancuch, -1 jesli nie ma lub pozycja str
print("Ala ma kota".find("ma")) # ma jest pod 4 znakiem 
print("Ala ma kota".find("tekst")) # -1 bo nie ma  
# rfing() wyszukuje od konca 

print("Ola ma psa, Ola ma kota".rfind("Ola"))

# likwiduje biale znaki od lewej 

print("\n \t   Test ". lstrip())
print(" Test \n \t   ".rstrip())

# kasuje biale znaki po obu stronach 
print(" \n \t Test \n \t".strip())
#Zmienia wystapienie w lancuchu na inny
# Kasia ma kota, Kasia ma psa
print("Ola ma kota, Ola ma psa".replace("Ola","Kasia"))

print("1256346".isalnum()) # True, lancuch jest liczba calkowita
print("1256346".isalpha()) # False 
print("Test".isalpha()) # True, lancuch z znakami alfabetu
print("Test 2".isalpha()) # False, bo liczba

print("test".islower()) #True, bo male litery 
print("  \t ".isspace()) #True, bo tylko biale znaki
print("HELLO".isupper()) # True, bo tylko wielkie litery

# laczy lancuchy w jeden string z separatorem 
print("-".join(["Ola", "Ania"]))

print(len("str length")) # 10 
print("HELLO World".lower()) # hello world
print("HELLO World".upper()) # HELLO WORLD 
print("HELLO world!".swapcase()) # hello WORLD!

print("My name is {myName}, I'm from {country}".format(myName = "Mateusz", country = "Poland"))
print("my name {0} and age {1}".format("mateusz",27))
print("my name {} and age {}".format("mateusz",27))
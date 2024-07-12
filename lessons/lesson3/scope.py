# Scope zasieg zmiennych - zmienne lokalne 
# Zmienne lokalne zadeklarowane sa np wewnatrz funkcji i tylko tam sa dostepne

number = 20 

def printNumber():
    print(number) # dostep do zmiennej globalnej, poniewa nie ma takiej w funkcji
    string = "test" # zadeklarowana zmienna lokalna
    print(string)

printNumber()

#id(string) # brak dostepu do string, bo jest zmienna lokalna funkcji 

# Zmienne posiadaja swoj zasieg, czyli obszar programu, ktory ma dostep do tych zmiennych. Zasieg wynika z blokow kodu wprowadzonych dzieki fynkcjom, klasom oraz modulom. Uwaga w python instrukcja if, petle, try / except nie definiuja zasiegu! 

# Zmienne globalne maja zasieg globalny, czyli dostepne sa w calym programie.

number = 12 # zmienna globalna 

print(number) # 12

if  number > 0:
    print(number) # instrukcja if ma dostep do zmiennej globalnej

def printNum():
    print(number) # funkcjia ma dostep do globalnej zmiennej 
printNum()

# zmienne lokalne o tej samej nazwie co globalne je sprzeslaniaja.
#  Podczas wywolywanie funkcji gdy potrzeby jest dostep do zmiennej Python sprawdza czy przypadkiem no tej samej nazwie nie jest zadeklarowana wewntrz funkcji, taka ma pierwszenstwo
# Jesli nie jest zdeklarowana wewnatrz funkcji to zmienna szukana jest stopien wyzej np. w globalnych zmiennych 


number = 20 

def printNumber():
    number = 6 # deklaracja zmiennej lokalnej o tej samej nazwie przeslania globalna
    print("number", number) # odwolanie po number odnosi sie do lokalnej zmiennej
printNumber()
print(number)

# podobna sytuacja jest z argumentami o takiej samej nazwie jak globalna, rowniez przesloni globalna


string = "hello"

def printData(string):
    print(1, string) # zmienna jako argument przeslania globalna o tej samej nazwie 

printData("test")
print(2, string)
print("------")
# Funkcja printData() przeslania zmienna globalna i wywoluje funkcje showinfo()
# Wywolana funkcja showInfo() odwolujaca sie do string w praktyce odwoluje sie do globalnego struing, a nie przeslonietego w printData()

string = "helloo"

def showInfo():
    print (3, string) # uwaga, odwolanie dio zmiennej globalnej! 

def printData():
    string = "test" # zmienna lokalna przeslania aglobalna
    print(2, string) # 2, Test 
    showInfo() # wywolanie funkcji showInfo
print(1, string)
printData()

# inna sytuacja jest gdy funkcja jesst zdefiniowana wewnatrz funkcji. Funkcja bar() odwolujaca sie do firstNum wyswietli 1, bo nie znaleziono definicji takiej zmiennej w bar(), lae znajduje sioe w funkcji test ktorej jest czescia 

firstNum = 9

def test():
    firstNum =1
    print("test() firstNum: ", firstNum)
    def bar():
        print("bar() firstNum: ", firstNum)
    bar()
    print("end test()")

print("global firstNum: ", firstNum)
test()

print("----------------")
# Czasem zachodzi potrzeba aby zmienic wartosc zmiennej globalnej z poziomu funkcji Wymagane jest uzycie slowa kluczowego globalnego aby nie utworzyc lokalnej zmiennej tylko wskazac ze chcemy operowac na globanlej zmiennej. Global pozwala zmodyfikowac zmienna poza swoim scope 

number = 20 

def printNumber():
    #nie modyfikujemuy globalnej tylko tworzymy lokalna zmienna! 
    number = 33 # nie zmieni globalnej
    print("doNumber()  : ", number)
printNumber()
print("global number", number)
print("--zm glob---")

number = 20 

def printNumber():
    global number # number wskazuje na globalna
    number = 33 # modyfikacja globalnej ! 
    print("doNumber() : ", number)
print("global number before", number)
printNumber()
print("global number after print number function", number)

# instrukcja if nie definiuje zasiegu podobnie jak petle i try / except ponizsza gobalna string bedzia nadpisana w instrukcji if 

if 1 == 1:
    print(1, string) 
    if 2 == 2:
        string = "test"
        print(2,string)
        if (3 == 3):
            print(3,string)
print(4,string)

print("------")

# Podobnie wewnatrz funkcji if nie definiuje zasiegu, odnosi sie dos tring zdefiniowanego lokalnie w funkcji 

string = "Hi"

def testFunc():
    string = "Local Hi"
    if 1 == 1:
        print(1, string) 
        if 2 == 2:
            string = "test"
            print(2,string)
            if (3 == 3):
                print(3,string)
    print(4,string)
testFunc()
print(5, string)
# Ograniczenie sposobu przekazania danych do funkcji - programistra za pomoca / oraz* moze okreslic dopuszczalne sposoby przekazywania argumentow do funkcji
# Slash oznacza parametry tylko pozycyjne , wazna jest kolejnosc tych parametrow i nie moga byc przekazywane jako argumenty nazwane. Uwaga parametry tylko pozycyjne umieszczane sa przed / dzieki temu rozdziela parametry tylko pozycyjne od reszty parametrow.

def printData(string, number =10, /):
    print(string, number);

printData("Test", 5) # dziala prawidlowo, argumenty pozycyjne : Test 5

 #  printData(string = "Test", number = 11) blad nie mozna uzywac argumentow nazwanych

 # Gwiazdka oznacza argumenty nazwane , musi byc umieszczona przed pierwszym parametrem, ktory ma byc tak przakazany 

def printData2(*, string, number =10):
   print(string, number);

printData2(string = "Test", number = 11)

#printData2("Test", 5) #nie dziala oba maja byc przekazane jako nazwane argumenty
def printData3(data,*, string, number =10):
   print(data, string, number);
printData3("tekst",string = "Test", number = 11)
# chodzi tu o to ze wszystkie argumenty po "*" musza byc nazwane natomiast w "/" wszystykie argumenty przed znakiem nie moga byc nazwane znaczy ze sa pozycyjne czyli

def printData4(float, bool, *, string, number = 10):
   print(float, bool, string, number);

printData4(12.5 , bool = True, string = "Test", number = 11)
printData4(float = 12.5, bool = False, number = 11, string = "Test")
printData4(20.3, False, number = 11, string = "Test")

# parametry po gwiazdce musza byc przekazane jako argumenty nazwane 
# parametry przed gwiazdka moga byc przekazane jako nazwane albo pozycyjne
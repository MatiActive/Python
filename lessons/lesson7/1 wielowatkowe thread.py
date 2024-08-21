# Watki - pozwalaja na podial programu na kilka rownolegle dzialajacych cześci aco daje mozliwość przyśpieszenia jego działania na procesorach z wieloma rdzeniami

# Wątki powstale w programie dziala sie dostepem do pamieci oraz zasobow co wymaga odpowiedniego zarządzania zwanego synchronizacja aby ustrzec sie przed potencjalnymi błedami, Przyładowo kiedy jeden watek zapisuje wartosc do zmiennej w momencie gdy inny watek probuje ja odczuytac co moze sie skonczyc bledna wartoscia

# Python daje nam do uzytku dwa moduły na pracę z watkami 
# _thread - nisko poziomowe api 
# threading - wysoko poziomowe api 

# _thread - proste wątki na bazie funkcji

import _thread, time

def printTime(threadName, sleepTime):
    num = 0 
    max = 6
    while num < max:
        localtime = time.localtime()
        info = time.strftime("%I:%M:%S", localtime)
        print(threadName, info)
        time.sleep(sleepTime)
        num += 1
    print(threadName, "ended.")

_thread.start_new_thread(printTime, ("BASIC thread", 1))
_thread.start_new_thread(printTime, ("Another thread", 2))

while 1 == 1:
    pass 

# Funkcja printTime będzie wątkiem powołanym do zycia dzieki funkcji _thread.start_new_thread() przyjmującej funkcję jako wątek oraz krotke argumentow przekazywanych tej funkcji. Rozpoczęcie wątku powoduje od razu dalsze wykonanie programu, dlatego aby sie nie zakonczyl potrzebna jest nieskonczona petla while time.sleep(x) usypia wątek na x sekund np. 05
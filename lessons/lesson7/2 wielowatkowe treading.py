import threading, time 

def printTime(threadName, sleeptime):
    num = 0
    max = 6 
    while num < max:
        localtime = time.localtime()
        print(threadName, time.strftime("%I:%M:%S", localtime))
        time.sleep(sleeptime)
        num += 1
    print(threadName, "ended.")

t1 = threading.Thread(target= printTime, args=("t1", 0.5))
t2 = threading.Thread(target= printTime, args=("t2", 2))
t1.start() # rozpoczyna dzialanie watku 
t2.start()
print("Główny wątek programu poczeka na zakończenie t1")
t1.join()
t2.join()
print("Main prog ended")

# Moduł threading rowniez pozwala na utworzenie watku z funkcji, ale zwraca obiekt do sterowania watkiem. Funckja start() rozpoczyna wątek, a join() sprawia, że głowny wątek programu poczeka na zakonczenie watku t1. Nieskończona pętla while juz nie jest potrzebna
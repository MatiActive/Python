# Synchronizacja watkow - ma na celu aby w danym momencie wiele watkow nie rywalizowało nadostep do zasobu, czyli tylko hjeden w danym czasie bedzie mogl odczytac i zapisac wartosc zasobu. Unika sie w ten sposob potencjalnych błędow

# Python korzysta z prostego mechanizmu blokowania watkow tzw. locking
# podstawą jest metoda treading.Lock(() zwraca mechanizm blokujacy. Udostepnia metodę acquire(blocking = True) która zmusza wszystkie watki aby zaczely dzialac synchronicznie dla danego kawalka kodu
# domyslnie opcjonalny parametr blocking ma wartosc True co sprawia, że jesli jakis watek pracuje nad danym zasobem to drugi watek poczeka na swoja kolej. Wartosc False sprawi ze nie bedzie czekał i bedzie kontynuował swoja prace 

# Oprócz acquire() istnieje druga wazna metoda release() która zwalnia blokowanie zasobu, dzieki czemu inny czekajacy watek moze z niego skorzystac

import threading, time
data = ["Ola", "Ania", "Yeti", "Kotleti","Daniel", "Adam", "Kasia"]
dataLock = threading.Lock()

class newThread(threading.Thread):
    def __init__(self, threadName, dataLen, sleeptime):
        threading.Thread.__init__(self)
        self.threadName = threadName
        self.dataLen = dataLen
        self.sleeptime = sleeptime

    def run(self):
        num = 0 
        while num < self.dataLen:
            dataLock.acquire()
            print(self.threadName, data[num])
            dataLock.release()
            time.sleep(self.sleeptime)
            num += 1 
        print(self.threadName, "ended.")

thread1 = newThread("thread1", len(data), 1)
thread1.start()
thread2 = newThread("thread2", len(data), 1)
thread2.start()
thread1.join()
thread2.join()
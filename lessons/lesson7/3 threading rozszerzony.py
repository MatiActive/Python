# treading - watek na bazie klasy rozszerzajacej Thread

import threading, time 

class newThread(threading.Thread):
    def __init__(self, threadName, sleepTime):
        threading.Thread.__init__(self)
        self.threadName = threadName
        self.sleepTime = sleepTime

    def run(self):
        num = 0
        while num < 5:
            localtime = time.localtime()
            info = time.strftime("%I:%M:%S", localtime)
            print(self.threadName, num, info )
            time.sleep(self.sleepTime)
            num += 1 
            if num == 3: break
        print(self.threadName, "ended.")

thread1 = newThread("thread1", 1)
thread1.start()
thread1.join()
# Klasa tworząc wątek musi rozszerzać treading.Thread oraz nadpisać metodę run() która bedzie wywoływana jak wątek rozpocznie swoja prace. w wątku jest dostęp do metody join(), isAlive() - czy działa oraz start() 
import threading, time

data = ["Mati", "Yeti", "Kotleti","Gothic"]
dataLock = threading.Lock()

class damnBoy(threading.Thread):
    def __init__(self, threadName, dataLen, sleeptime):
        threading.Thread.__init__(self)
        self.threadName = threadName
        self.dataLen = dataLen
        self.sleeptime = sleeptime

    def run(self):
        num = 0 
        while num < self.dataLen:
            localtime = time.localtime()
            info = time.strftime("%H:%M:%S", localtime)
            dataLock.acquire()
            data[num] = data[num] + " - " + str(num)
            print(self.threadName, data[num] + " --> " + info)
            dataLock.release()
            time.sleep(self.sleeptime)
            num += 1
        print(self.threadName, "ended.")
thred1 = damnBoy("t1", len(data), 1)
thred2 = damnBoy("t2", len(data), 1)
thred1.start()
thred2.start()
#time.sleep(1)
#print("---thread 2 status : ", thred2.is_alive())
thred1.join()
thred2.join()

        
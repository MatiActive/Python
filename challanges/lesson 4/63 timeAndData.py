import datetime
import time 
import random 

startTime = time.perf_counter()
time.sleep(0.1)
endTime = time.perf_counter()
result = endTime - startTime
print(result)
if result >= 3:
    print("za dlugi czas")
else:
    print("czas wystarczajaco krotki")

start_time = datetime.datetime.now()
print("Czas rozpoczecia zadania:", start_time.strftime("%H:%M:%S %d.%m.%Y"))

sleep_time = random.randint(1,5)
time.sleep(sleep_time)
end_time = datetime.datetime.now()
print("zakonczenie zadania:", end_time.strftime("%H:%M:%S %d.%m.%Y"))

result2 = end_time - start_time
print(result2)
if result2.total_seconds() >= 3:
    print("za dlugi czas")
else:
    print("czas wystarczajaco krotki")
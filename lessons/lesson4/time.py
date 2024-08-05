# PRACA Z CZASEM I DATAMI 
# czas w komputerach w najprostszy sposob najczesciej wyrazony jest w postaci ilosci sekund od 1 stycznia 1970r, nazzywamy taka wartosc epoch czyli timestampem. Python udostepnia wiele funkcji do operowania na datach ddostepnych w module time

import time 

ticks = time.time()
print(ticks) # 1722554156.360188 sekund od 1970 r :D

# Bardziej przystepna funkcjia wracajaca aktualnay czas jest time.localtime() ktora zwraca zarowno date jak rowniez czas w formie przystepnej krotki (tzw named tumpe)

timeData = time.localtime()
print(timeData) # time.struct_time(tm_year=2024, tm_mon=8, tm_mday=2, tm_hour=1, tm_min=21, tm_sec=28, tm_wday=4, tm_yday=215, tm_isdst=1)
print(timeData.tm_year) # 2024 -- rok
print(timeData.tm_mon) # 8 -- miesiac
print(timeData.tm_mday) # 2 -- dzien miesiaca 
print(timeData.tm_hour) # 1 -- godzina 
print(timeData.tm_min) # 24 -- minuty
print(timeData.tm_sec) # 12 -- sekundy
print(timeData.tm_wday) # dzien tygodnia od 0 do 6 0 to poniedzialek 
print(timeData.tm_yday) # 215 dzien roku od 1 do 366 
print(timeData.tm_isdst) # 1 czas letni badz nie 1 to letni

# Do funkcji time.localtime() mozna przekazac rowniez timestamp czyli sekundy od 01.01.1970

timedata = time.localtime(0)
print(timedata) # time.struct_time(tm_year=1970, tm_mon=1, tm_mday=1, tm_hour=1, tm_min=0, tm_sec=0, tm_wday=3, tm_yday=1, tm_isdst=0)

ticks = time.time()
print(ticks) # 1722555267.9472406

timedata = time.localtime(ticks - (24 * 60 * 60))
print(timedata) #time.struct_time(tm_year=2024, tm_mon=8, tm_mday=1, tm_hour=1, tm_min=35, tm_sec=51, tm_wday=3, tm_yday=214, tm_isdst=1) odjety jeden dzien

# funkcja time.asctime() formatuje w wygodny sposob date i czas dostarczona przez time.localtime()

result = time.asctime(time.localtime(time.time()))
print("wynik: ", result) # wynik:  Fri Aug  2 01:42:54 2024

# Funkcja time.strftime() formatuje data i czas na string wedlug podanego wzorca, korzysta z oznaczeni ktore beda zastapione konkretnymi wartosciami w tekscie : %Y-rok , %m-miesiac , %d-dzien , %H-godzina , %M-minuty , %S-sekundy

timeData =  time.localtime() # aktualny czas 
timeStr = time.strftime("%m/%d/%Y  %H:%M:%S")
print(timeStr) # 08/02/2024  01:50:53

# funkcja time.strptime() parsuje lancuch znakow i tworzy z niego krotke z ata i czasem 

timeStr = "02 March, 2025"
timeData = time.strptime(timeStr, "%d %B, %Y") # d- dzien B- nazwa miesiaca Y-rok

print(timeData) # time.struct_time(tm_year=2025, tm_mon=3, tm_mday=2, tm_hour=0, tm_min=0, tm_sec=0, tm_wday=6, tm_yday=61, tm_isdst=-1)

# funkcja time.sleep() usypia glowny watek programu na okreslona ilosc sekund 

#i = 0
#while i < 5: 
#    time.sleep(1) # usypia watek programu na sekunde 
#    print( time.asctime(time.localtime()))
#    i += 1
# Fri Aug  2 02:00:22 2024
# Fri Aug  2 02:00:23 2024
# Fri Aug  2 02:00:24 2024
# Fri Aug  2 02:00:25 2024
# Fri Aug  2 02:00:26 2024

# pomiar czasu wykonania programu 

tStart = time.perf_counter()
time.sleep(0.1)
tEnd = time.perf_counter()
#measure wall time
interval = tEnd - tStart
print("elapsed time: ", interval, "second") # elapsed time:  0.1001344970009086 second

import datetime

datetimeObj = datetime.datetime(2024, 7, 2)
datetime = datetime.datetime(2025, 5, 30, 23, 59, 0)
datetimeObj = datetime.now() # aktualny czas i data 

print("date(): ", datetimeObj.date())# date():  2024-08-02
print("time(): ", datetimeObj.time())# time():  02:22:50.004848
print("timestamp(): ", datetimeObj.timestamp())# timestamp():  1722558170.004848
print("weekday(): ", datetimeObj.weekday())# weekday():  4
print("today(): ", datetimeObj.today())# today():  2024-08-02 02:22:50.004976
print("year(): ", datetimeObj.year)# year():  2024
print("hour(): ", datetimeObj.hour)# hour():  2
print("minute(): ", datetimeObj.minute)# minute():  22
print("second(): ", datetimeObj.second)# second():  50
print("microsecond(): ", datetimeObj.microsecond)# microsecond():  4848
print("format(): ", datetimeObj.strftime("%m/%d/%Y %H:%M:%S")) # format():  08/02/2024 02:22:50
import datetime
datetime1 = datetime.datetime(2025, 5, 30, 23, 59, 0)
datetime2 = datetime.datetime(2025, 5, 30, 23, 59, 10)

print(datetime1 > datetime2) # False

date1 = datetime.date(2019, 4, 16)
date2 = datetime.date(2020, 11, 3)

print(date1 > date2) # FALSE
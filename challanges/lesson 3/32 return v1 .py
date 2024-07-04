
hour = 3
minutes = 25

def convertToSeconds(a, b):
    minutes = (a * 60) + b
    second = minutes * 60
    return second
c = convertToSeconds ( hour,minutes)
print(c)

def convertToHours(minutes):
    minToHour = minutes / 60
    return minToHour
d = convertToHours (120)
print(d)


# a tak zrobil na zajeciach 

def convertToSeconds2(hours, minutes):
    return minutes * 60 + (hours * 60 *60)

def convertToHours2(minutes):
    return minutes /60

seconds = convertToSeconds2(3,25)
print("ilosc sekund : ", seconds)

hours = convertToHours2(120)
print("ilosc godzin", hours)
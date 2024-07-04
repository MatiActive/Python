ageLimit = 10 
heightLimit = 140

age = int(input("podaj swoj wiek : "))
height = int(input("podaj swoj wzrost : "))

if age >= ageLimit and height >= heightLimit:
    print("mozesz wejsc na kolejke")
else:
    print("nie masz wstepu na kolejke")
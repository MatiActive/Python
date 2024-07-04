str = "Hello Kurwa!!!"
print(str)
print("ilosc znakow str :",len(str))
print("typ stringa ", type(str))
print("wyswietlony 3 znak :",str[2])
print("wyswietlony od 3 do 5 znaku :",str[2:5])
print("wyswietlony od 4 do konca :", str[5:])
longString = """ Wzór na wskaźnik BMI – jak obliczyć? Obliczenie wskaźnika BMI jest bardzo proste. Aby móc to zrobić, potrzebne są dwie dane: wzrost i aktualna masa ciała. Następnie należy podzielić wagę wyrażoną w kilogramach przez wzrost podniesiony do kwadratu, wyrażony w metrach, czyli w skrócie BMI = kg / m2. """
print(longString)
print("ilosc znakow long string :", len(longString))

strWithBreakLine = "Światła miasta\n migotały w \"rytm\" \tpadającego deszczu."
print("Tekst z zasotsowaniem nowej lini i tabulatora :", strWithBreakLine)

word1 = "Help"
word2 = "stringy"
word3 = "architect"
word4 = "Azurh"
word5 = "Go"
word6 = "Selection"

#( word1[len((word1))-1]) word1 to slowo Help ktore ma znakow 4 a minus jeden dlatego ze python liczy od 0 wiec zeby wyswietlic ostatnia litere musimy odjac 1 

print( word1[len((word1))-1])
print( word2[len((word2))-1])
print( word3[len((word3))-1])
print( word4[len((word4))-1])
print( word5[len((word5))-1])
print( word6[len((word6))-1])

tekst = "Światła miasta migotały w rytm padającego deszczu."

print("co trzecia litera tekstu :", tekst[::3])
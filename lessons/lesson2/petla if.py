# if - innstrukacja warunkowa do podejmowania decyzji w programie w trakcie dzialania programu moze dojsc do roznych sytuacji na ktore bedzie musiala aplikacja zareagowac np dzialania uzytkownika, nowe dane pobrane z sieci itp. podejmowanie decyzji zwykle odbywa sie z wykorzystaniem instrukcji warunkowej if oraz kombinacji if else 

# instrukcja if warunkuje wywolanie wyrazenie i jesli jego rezultat bedzie true to wykona blok kodu (uwaga na wciecia!)

#przyklad 
print("---if---")
number = 10

if number > 6:
    print("number wieksze od 6")
    print("tez sie wyswietli jesli numer > 6 ")

if number == 2:
    print("number rowne 2")

print("---elif---")
# elif - jesli instrukcja if nie spelnia warunkow urochomi kolejna po elif dzieki temu mozna sprawdzic wiele wariantow 

num = 20 

if num == 7:
    print("num jest 7")
elif num == 10:
    print("num jest 10")
elif num == 12:
    print("num jest 12")
elif num == 14:
    print("num jest 14")
elif num >= 15:
    print("num jest  wieksze rowne 15")
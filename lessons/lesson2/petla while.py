# ppetla while wykonuje sie tak dlugo jak warunek jest spelniony czyli zwraca true. gdy warunek jest je spelniony to kontrola programu przechodzi do kolejnej instrukcji za petla 

number =4 
while number > 0:
    print(number)
    number = number -1
print("kod po petli")

# na poczatku petli while sprawdzane jes czy numer o wartosci 4 jest wieksze od 0 co zwraca true wiec nastapi pierwsza iteracja petli nastepnie wyswietli sie tekst i licznuik zmiejszany jest o jeden ponownie sprawdzany jest warunek number jest wieksze od 0 itd.

# mozna laczyc z else 
number = 0 
while number <3:
    print(number)
    number += 1
else:
    print("koniec bo number jest"+ " " + str(number) + " " +"czyli nie spenia warunku < 3" ) 
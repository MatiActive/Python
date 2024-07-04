number  = 5 
print(type(number))
addr = id(number)
number += 2
addr2 = id(number)
print("nie sa takie same", addr, addr2)

fruits = ["orange", "apple", "bannana", "cherry"]
addr3 = id(fruits)
fruits += ["orange"]
fruits.append("pomidor")#inny sposob dodania do listy 
print(fruits)
addr4 = id(fruits)
print("sa takie same tzn mutowalne", addr3, addr4 )

# Roznica miedzy typami mutowalnymi a niemutowalnymi jest taka ze w typach mutowalnych nie jest tworzona nowa dana nie zmienia sie id tylko wartosci sa dodawane nie tworzona dowa zmienna a niemutowalne sa to takie wartosci ktore po zamianie wartosci tworzona jest nowa zmienna i nowe miejsce w pamieci o innym id
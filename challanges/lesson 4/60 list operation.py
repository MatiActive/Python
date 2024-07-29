guests = ["Bartek", "Rafal", "Mateusz", "Sylwia", "Karolina"]
print("ilosc gosci: ", len(guests))

guests.extend(["Malwina", "Tomasz"])
print(guests)
guests.remove("Bartek")
print(guests)
guests.sort()
print(guests)
dishes = ["Frytki", "Pomidorowa", "schabowy"]
dishes.extend(["salatka", "ryba"])
middledishes = dishes[len(dishes) // 2]
print("potrawa na srodku lissty: ",middledishes)
print("usuwana potrawa: ",dishes.pop())
print("dania po usunieciu potrawy: ",dishes)

if "pizza" in dishes:
    print("pizza na liscie")
else:
    dishes.append("pizza")
print(dishes)
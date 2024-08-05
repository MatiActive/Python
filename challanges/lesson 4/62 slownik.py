print("--1--")
addressBook = {
    "Jan Kowalski": {"city": "gdansk", "postcode" : "80-000"}
          }
print(addressBook)
print("--2--")
SecondPerson = "Anna Nowak"
addressBook[SecondPerson] = {"city": "krakow", "postcode" : "00-001"}
print(addressBook)
print("--3--")
del addressBook["Jan Kowalski"]
print(addressBook)
print("--4--")
bookcopy = addressBook.copy()
print(bookcopy)
print("czy zawartosc jest identyczna", addressBook == bookcopy)
print("czy referencje sa identyczne", addressBook is bookcopy)
print("--5--")
found = False
for person in addressBook.values():
    if person["city"] == "krakow":
        found= True
        print("w ksiazce adresowej jest osoba  z krakowa")

if not found:
    print("w ksiazce nie ma osoby z krakowa")
print("--6--")
print(addressBook.keys())
print(addressBook.values())
# Stwórz klasę SimCard reprezentującą kartę sim telefonu z kontaktami
# 1) Klasa ustawia atrybut/zmienną klasy contacts jako listę w konstruktorze
# 2) Dodaj metodę addContact przyjmującą oprócz self również parametry
#    name i telephone. Sprawdź z funkcją isinstance czy przekazane dane są
#    prawidłowe, czyli str i int. Stwórz słowik z name i telephone i dodaj go 
#    do listy kontaktów obiektu powstałego na bazie klasy
# 3) Napisz metodę showContacts, która w pętli pokaże kolejne kontakty w terminalu
# 4) Stwórz instancję klasy SimCard
# 5) Dodaj poniższe kontakty:
#    - "Ola", 98765432
#    - "Adam", 12345678
#    - 100, 12345678
#    - "Kasia", "numer"
#    Część danych jest nieprawidłowa, więc nie powinny być dodane przez addContact
# 6) Wyświetl kontakty z showContacts()

class SimCard:
    def __init__(self):
        self.contact = []
    def addContact(self, name, telephone):
        if isinstance(name, str) == False: return
        if isinstance(telephone, int) == False: return

        kontakt = {
            "name" : name,
            "telephone" : telephone
        }
        self.contact.append(kontakt)

    def showContact(self):
        for x in self.contact:
            print(x["name"] + " " + str(x["telephone"]))

sim = SimCard()
sim.addContact("Ola", 98765432)
sim.addContact("Adam", 12345678)
sim.addContact(100, 12345678)
sim.addContact("Kasia", "numer")
sim.showContact()
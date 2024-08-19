from classImport import User, Surname

class Age(Surname):
    def __init__(self, name, surname,Age):
        Surname.__init__(self,name, surname)
        self.Age = Age
    def __str__(self):
        return Surname.__str__(self) + " " + "Age : " + self.Age
    
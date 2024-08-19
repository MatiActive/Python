class User:
    def __init__(self, name):
        self.name = name 

    def __str__(self):
        return "First Name: " + self.name

class Surname(User):
    def __init__(self, name, surname):
        User.__init__(self,name)
        self.surname = surname
    def __str__(self):
        return User.__str__(self)+ " " "Surname : "+ self.surname

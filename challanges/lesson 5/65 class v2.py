class User:

    def __init__(self, name, password):
        self.name = name
        self.password = password

    def changePassword(self, oldPassword, newPassword):
        if self.password == oldPassword:
            self.newPassword = newPassword
            print("haslo zostalo zmnienione")
        else: print("nieprawidlowe dane")
user = User("adam", "admin")
user.changePassword("name","pass")
user.changePassword("admin","pass")
user.changePassword("pass","kwas")
user.changePassword("admin","kwas")
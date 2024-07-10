def createUserProfile(firstName, lastName, age, city):
    return {"firstName" :firstName, "lastName" : lastName, "age" : age,"city" : city}


firstName = input("podaj swoje imie :")
lastName = input("podaj swoje nazwisko :")
age = input("podaj swoje wiek :")
city = input("podaj swoje miasto :")

userProfile = createUserProfile(firstName=firstName, lastName=lastName, age=age,city=city)

for key, value in userProfile.items():
    print( key + " : " +  value)
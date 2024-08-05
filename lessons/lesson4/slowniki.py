data = { "name" : "kasia", "city" : "waw" }
print(data["name"]) # pobranie elementu zkey name, kasia
data["name"] = "ola" # modyfikacja elementy 

emailKey = "email"
data[emailKey] = "ola@example.com"
print(data) # {'name': 'ola', 'city': 'waw', 'email': 'ola@example.com'}

del data["city"] # skasowanie elementu

print(data) # {'name': 'ola', 'email': 'ola@example.com'}

data.clear() # skasowanie wszzystkich elementow
print(data) # {}

data = {"name" : "ola", "city" : "wwa"}
print(len(data)) # dlugosc slownika: 2 elementy 

copy = data.copy() # tworzy plaska kopie slownika
print(copy) # {'name': 'ola', 'city': 'wwa'}
print(data["name"] is copy["name"]) # True to samo miejsce w pamieci 
print(data is copy) # False wartosci to te samo miejsce w pamieci ale slownik juz nie 
# tworzy slownik z podanymi kluczami, wartosc jako none
print(data.fromkeys(("name", "email", "country")))
#{'name': None, 'email': None, 'country': None}
data2 = dict.fromkeys(("name", "city", "code")) # 
print(data2) # {'name': None, 'city': None, 'code': None}
data3 = dict.fromkeys(("name", "city", "code"),0) # 
print(data3) # {'name': 0, 'city': 0, 'code': 0}

# zwraca istniejaca wartosc klucza lub drugi argument
print(data.get("postal code", "DEFAULT")) # DEFAULT

print("name" in data) # czy kluc jest w slowniku, True

print(data.keys()) # zwraca liste kluczy: dict_keys(['name', 'city'])

print(data.values()) # zwraca liste wartosci: dict_values(['ola', 'wwa'])

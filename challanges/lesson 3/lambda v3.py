from functools import reduce
users = [
    {'name': 'jan' , 'age': 15},
    {'name': 'anna' , 'age': 25},
    {'name': 'piotr' , 'age': 30},
    {'name': 'katarzyna' , 'age': 22}
]

adult = filter(lambda user: user["age"] > 18, users )
adult = list(adult)
print(adult)

agex2 = map(lambda user: user["age"] * 2 , adult)
agex2 = list(agex2)
print(agex2)

sumAge = reduce(lambda x,y : x +y , agex2)
print(sumAge)
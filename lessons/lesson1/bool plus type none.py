#false valuse, czyli wartosci ktore daja false przy konwersji na boolean
print(bool())
print(bool(0) )
print(bool(0.0))
print(bool( () ))
print(bool( [] ))
print(bool( {} ))
print(bool( '' ))
print(bool( None ))
#true values

print(bool(True))
print(bool(1))
print(bool(5))
print(bool(-10))
print(bool(("Ola", 1)))
print(bool( [0] ))
print(bool( {0} ))
print(bool( "x " ))

#none
data = None

print(type(data))

if data is True:
    print("data is true")
elif data is False:
    print("data is false")
else:
    print("none is none")
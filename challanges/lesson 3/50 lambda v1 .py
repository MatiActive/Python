listData = ["ola", "ania", "kasia"]

result = map(lambda a: a + " kowalska", listData)
result = list(result)
print(result)

lenght = filter(lambda a: len(a) > 12, result )
print(list(lenght))
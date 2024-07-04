nested_list = [
    [1, 2, 3],
    ['a','b','c'],
    [True, False, True]
]
for listKey in nested_list:
    for listValue in listKey:
        print(listValue)
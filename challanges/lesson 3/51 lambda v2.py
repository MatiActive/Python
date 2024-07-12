from functools import reduce
listData = [3,4,5,3,4,6]

sum = reduce(lambda a,b: a+b, listData)
print(sum)
sr = sum / len(listData)
print(sr)
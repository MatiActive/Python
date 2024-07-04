firstName = "mateusz"
lastName = "narkiewicz"
fullname = firstName + " " + lastName
print(fullname)

listOne = [1,2,3]
listTwo = [4,5,6]
combinedList= listOne + listTwo
print(combinedList)
print(len(combinedList))

if len(combinedList) > 5:
    print("lista jest za dluga")
else:
    print("lista jest ok")


greeting = "hello" + " " + fullname

if "hello" in greeting:
    print(greeting)
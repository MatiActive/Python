
def findLargest(num1, num2):
    if num1 > num2:
        print("num1 jest wieksze : ", num1)
        return num1
    elif num2 > num1:
        print("num2 jest wieksze : ", num2)
        return num2
    else:
        print("num1 jest rowne num2 : " + str(num1)+ " " +" = " +" " +str(num2))

c = findLargest(12,12)

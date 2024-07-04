BMI = 70 / (1.75 * 1.75)
print("wartosc BMI wynosci :",  BMI)
print("typ zmiennej", type(BMI))

if BMI > 24.9:
    print("za wysokie")
elif BMI < 18.5:
    print("za niskie")
else:
    print("wzorowe")
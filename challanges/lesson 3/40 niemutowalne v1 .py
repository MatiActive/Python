def increaseSalary(money, bonus):
    money = money * 1.2
    return money + bonus

salary = 5000
print("salary : ",salary)
newSalary = increaseSalary(salary,1000)
print("salary: ",newSalary)


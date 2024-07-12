employees = []


def addEmployee(email,salary):
    user = {
        "email" : email,
        "salary" : salary 
    }
    employees.append(user)

addEmployee("mati@mgail.com", 6000)
addEmployee("mati2@mgail.com", 8000)
addEmployee("mati3@mgail.com", 10000)

def increaseSalary(employees, pctIncrease):
    pctIncrease *= 0.01
    for user in employees:
        user["salary"] *= 1 + pctIncrease
increaseSalary(employees,  20)
print(employees)
import random
class Student:
    def __init__(self, name, surname, age, city):
        self.name = name
        self.surname = surname
        self.age = age
        self.city = city
        self.schoolName = None
        self.fieldOfStudy = None

    def PrintStudentData(self):
        print(self.name, self.surname, self.age, self.city, self.schoolName, self.fieldOfStudy)

class School:
    def __init__(self, name, city):
        self.name = name
        self.city = city
        self.studentList = []
        self.fieldOfStudy = ["IT", "Math", "Robotics"]

    def addStudent(self, student):
        if isinstance(student, Student):
            self.studentList.append(student)
            student.schoolName = self.name
            student.fieldOfStudy = random.choice(self.fieldOfStudy)
    def printSchoolData(self):
        print("school name : ", self.name, "city : ", self.city)
        print("students : ")
        for i in self.studentList:
            i.PrintStudentData()

student1 = Student("Sylwia", "Sendyk", 28, "Byd")
#student1.schoolName ="Tech school"
#student1.country = "Poland"
#student1.PrintStudentData()
#print(student1.country)
student2 = Student("Bartosz", "Rogowicz", 27, "Biz")
student3 = Student("Sylwia", "Narkiewicz", 28, "Bed")
student4 = Student("Rafal", "Grab", 27, "Kad")
school = School("Tech school", "Byd")
school2 = School("Informatic", " Oln" )
school.addStudent(student1)
school.addStudent(student2)
school2.addStudent(student3)
school2.addStudent(student4)

school.printSchoolData()
school2.printSchoolData()

# 작성자: 김민재
# 작성일: 2026.10.13

class Department:
    def __init__(self, name):
        self.name = name
        self.courses = []

    def add_course(self, name, credit):
        course = Course(name, credit)
        self.courses.append(course)
        return course


class Course:
    def __init__(self, name, credit):
        self.name = name
        self.credit = credit
        self.students = []


class Student:
    def __init__(self, name, student_id):
        self.name = name
        self.student_id = student_id
        self.courses = []

    def enroll(self, course):
        self.courses.append(course)
        course.students.append(self)


dept = Department("컴퓨터")
math1 = dept.add_course("공업수학", 3)
math2 = dept.add_course("이산수학", 2)

hwang = Student("Hwang", 202611852)
hwang.enroll(math1)

print(dept.name)
print(math1.name, math1.credit)
print(hwang.name, hwang.student_id)
print(hwang.courses[0].name)
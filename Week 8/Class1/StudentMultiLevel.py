class Person:
    def __init__(self):
            self.a = 1

class Student(Person):
    def __init__(self):
            self.b = 2

class GradStudent(Student):
    def __init__(self):
            self.c = 3
            super().b = 6

grad_student_1 = GradStudent()

grad_student_1.a = 6
grad_student_1.b = 71
grad_student_1.c = 72

x=3

class Student:

    def __init__(self, id: int, name, gpa: float):

        self.id = id
        self.name = name
        self.gpa = gpa


class StudentClass:

    def __init__(self):

        self.__student_list = []

    def add_student(self, student: Student):
# enforced the type we are adding. This allows us to calculate things like average GPA. Without this, could enter
# string as a student.
        self.__student_list.append(student)

    def remove_student(self, student_id):
        """This deletes a student, return True on successful delete."""
        for current_student in self.__student_list:
            if current_student.id == student_id:
# enforcing the entering of an integer
                self.__student_list.remove(current_student)
                return True
        return False
# this lets you know if integer entered

    def list_students(self):

        for student in self.__student_list:
            print ("Student ID: " + str(student.id) + " Student Name: " + student.name)

    def get_count_of_students(self):

        return len(self.__student_list)

    def get_average_gpa(self):
        #need to write a loop
        gpa_total = 0
        for student in self.__student_list:
            gpa_total += student.gpa

        #return gpa_total / len(self.__student_list)
        return gpa_total / self.get_count_of_students()




math_101 = StudentClass()

s1 = Student(100, "Mary", 3.5)
s2 = Student(200, "Bob", 4.0)

s3 = Student(300, "Brendan", 3.6)

math_101.add_student(s1)
math_101.add_student(s2)
math_101.add_student(s3)
math_101.remove_student(200)

math_101.list_students()

print("The number of students left in this class is " + str(math_101.get_count_of_students()))

print ("The average GPA of the remaining students is " + str(math_101.get_average_gpa()))

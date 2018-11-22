students = [[88,99,10],[90,60,77],[80,90,90],[12,13,14]]
#what is the value of the first quiz of the second student.
#need to determine how many dimensions. In this case the overall list is the first dimension and the grades is the second.
# 1st quiz for second student
print(students[1][0])

#highest quiz of student 2
#tradtionally we would do
#test = [1,2,3,4]
#print(max(test))
print(max(students[1]))

# What is the average of quizzes for students #3
print(sum(students[2])/len(students[2]))


#How to create third dimentsion with

students2 = [[[40,50], [55,30]],[[30, 40],[22,10]]]
#2 students that did 2 quizzes in 2 sections
# What is the score of section1 of quiz1 for student1
print(students2[0][0][0])

#print the results that the forth student got.
students3 = [[88,99,10],[90,60,77],[80,90,90],[12,13,14]]
for q in students3[3]:
    print(q)

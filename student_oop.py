from student import Student
# print(Student.count)

s1 = Student('mehul', 'm', 10, 90.5) # 3002
'''
1 - memory is reserved in the RAM object : 3002
2 - Student.__init__(3002, 'mehul', 'm', 10, 90.5)
'''

'''s1.name = 'mehul'
s1.gender = 'm'
s1.roll = 10
s1.marks = 90.5'''


s2 = Student('jane', 'f', 11, 45) # 3004
'''
1 - memory is reserved in the RAM object : 3004
2 - Student.__init__(3004, 'mehul', 'm', 10, 90.5)
'''

'''s2.name = 'jane'
s2.gender = 'f'
s2.roll = 11
s2.marks = 89'''

# print(s1.getgrade()) # Student.getgrade(s1)
# print(s2.getgrade())

# print(Student.count)

# print(type(s1))
# print(type(s2))

# print(s1.getdetails())
# Student.getdetails(s1)

# print(s2.getdetails())
# Student.getdetails(s2)

'''print(s1.name)
print(s2.name)
print(s1.roll)
print(s2.gender)'''

s3 = Student('jill', 'f', 13, 90)

s3.studentname = 'jill'
s3.gen = 'f'
s3.roll = 13
s3.m = 90

'''print(s1.name)
print(s2.name)
print(s3.name)'''

# print(Student.count)

studentlist = [s1, s2, s3]
'''for student in studentlist:
  print(student.getdetails())'''

# get a new list of student names who have scored above 80
above80 = [student.name for student in studentlist if student.marks > 80]
for name in above80:
  print(name)
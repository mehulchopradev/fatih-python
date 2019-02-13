from student import Student
from professor import Professor
from photosession import takephoto

s1 = Student(name='mehul', gender='m', roll=10, marks=90)
# Student.__init__(4003, name='mehul', gender='m', roll=10, marks=90)

p1 = Professor(name='fatih', gender='m', subjects=['Physics','Maths'], contactnos=['9879897','9878686878'])
# Professor.__init__(4005, name='fatih', gender='m', subjects=['Physics','Maths'])

# print(s1.name)
# print(p1.name)

# print(s1.getdetails())
# Student.getdetails(s1)

# print(p1.getdetails())
# Professor.getdetails(p1)

name = 'mehul'
print(name)
# print(name.__str__())

print(p1)
print(s1)
# print(p1.__str__())

takephoto(s1)
takephoto(p1)
takephoto('mehul')
# able to represent an actor in the real world as some data reserved in the RAM
  # actor - object
  # object - data type (user defined data type)
  # class - from a class I can create n objects.
  # a class defines a data type for an object

  # actor characteristics - object attributes (name, gender, roll, marks)

class Student:
  def __init__(self, name, gender, roll, marks):
    # constructor
    self.name = name
    self.gender = gender
    self.roll = roll
    self.marks = marks

s1 = Student('mehul', 'm', 10, 90.5) # 3002
'''
1 - memory is reserved in the RAM object : 3002
2 - Student.__init__(3002, 'mehul', 'm', 10, 90.5)
'''

'''s1.name = 'mehul'
s1.gender = 'm'
s1.roll = 10
s1.marks = 90.5'''


s2 = Student('jane', 'f', 11, 89) # 3004
'''
1 - memory is reserved in the RAM object : 3004
2 - Student.__init__(3004, 'mehul', 'm', 10, 90.5)
'''

'''s2.name = 'jane'
s2.gender = 'f'
s2.roll = 11
s2.marks = 89'''

# print(type(s1))
# print(type(s2))

'''print(s1.name)
print(s2.name)
print(s1.roll)
print(s2.gender)'''

s3 = Student('jill', 'f', 13, 90)

s3.studentname = 'jill'
s3.gen = 'f'
s3.roll = 13
s3.m = 90

print(s1.name)
print(s2.name)
print(s3.name)
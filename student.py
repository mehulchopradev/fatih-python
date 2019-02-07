# able to represent an actor in the real world as some data reserved in the RAM
  # actor - object
  # object - data type (user defined data type)
  # class - from a class I can create n objects.
  # a class defines a data type for an object

  # actor characteristics - object attributes (name, gender, roll, marks)
  # real world actions happen on actors - methods to be called on the respective objects

class Student:

  # class attribute
  count = 0

  def __init__(self, name, gender, roll, marks, contactnos=[]):
    # constructor

    # object attributes
    self.name = name
    self.gender = gender
    self.roll = roll
    self.marks = marks
    if isinstance(contactnos, list):
      self.contactnos = contactnos
    else:
      self.contactnos = []

    # increment
    Student.count += 1 # access a class attribute

  def getdetails(self):
    part1 = 'Name : ' + self.name + '\nGender : ' + self.gender + '\nRoll : ' + str(self.roll)\
    + '\nMarks : ' + str(self.marks) + '\n'

    if self.contactnos:
      part2 = '|'.join(self.contactnos)
    else:
      part2 = 'No contact nos'

    return part1 + part2


  def getgrade(self):
    marks = self.marks
    if marks > 100 or marks < 0:
      return 'I'
    elif marks >= 70:
      return 'A'
    elif marks >= 60:
      return 'B'
    elif marks >= 40:
      return 'C'
    else:
      return 'F'

# print(__name__)

# when run the module itself - __main__
# when run as part of import in another module - student

if __name__ == '__main__':
  s1 = Student(name='fatih', gender='m', marks=45, roll=10, contactnos=['86868768'])
  print(s1.getdetails())
  print(s1.getgrade())
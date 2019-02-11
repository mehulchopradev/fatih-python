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
    self.__gender = gender # private to the class student
    self.__roll = roll # private
    self.marks = marks
    if isinstance(contactnos, list):
      self.contactnos = contactnos
    else:
      self.contactnos = []

    # increment
    Student.count += 1 # access a class attribute

  def getdetails(self):
    '''part1 = 'Name : ' + self.name + '\nGender : ' + self.gender + '\nRoll : ' + str(self.roll)\
    + '\nMarks : ' + str(self.marks) + '\n' '''

    # part1 = 'Name : {0}\nGender : {1}\nRoll : {2}\nMarks : {3}'.format(self.name, self.gender, self.roll, self.marks)
    # part1 = 'Name : {name}\nGender : {gender}\nRoll : {roll}\n'.format(name=self.name, gender=self.gender, roll=self.roll)

    part1 = f'Name: {self.name}\nGender : {self.__gender}\nRoll : {self.__roll}\nMarks : {self.marks}'

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

  def getnameroll(self):
    return (self.name, self.roll)

  # Encapsulation
  def setroll(self, roll):
    if roll > 0:
      self.__roll = roll

  def getroll(self):
    return self.__roll


# print(__name__)

# when run the module itself - __main__
# when run as part of import in another module - student

if __name__ == '__main__':
  s1 = Student(name='fatih', gender='m', marks=45, roll=10, contactnos=['86868768'])
  s1.__gender = 'o' # still not work
  s1.__roll = -10
  s1.setroll(12)
  print(s1.getroll())
  # print(s1.getdetails())
  # print(s1.getgrade())
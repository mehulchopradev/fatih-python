# able to represent an actor in the real world as some data reserved in the RAM
  # actor - object
  # object - data type (user defined data type)
  # class - from a class I can create n objects.
  # a class defines a data type for an object

  # actor characteristics - object attributes (name, gender, roll, marks)
  # real world actions happen on actors - methods to be called on the respective objects

from address import Address # composition association

class Student:

  # class attribute
  count = 0

  def __init__(self, name, gender, roll, marks, contactnos=[], address=None):
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

    if isinstance(address, Address):
      self.address = address
    else:
      self.address = None

    # increment
    Student.count += 1 # access a class attribute

  def getdetails(self):
    '''part1 = 'Name : ' + self.name + '\nGender : ' + self.gender + '\nRoll : ' + str(self.roll)\
    + '\nMarks : ' + str(self.marks) + '\n' '''

    # part1 = 'Name : {0}\nGender : {1}\nRoll : {2}\nMarks : {3}'.format(self.name, self.gender, self.roll, self.marks)
    # part1 = 'Name : {name}\nGender : {gender}\nRoll : {roll}\n'.format(name=self.name, gender=self.gender, roll=self.roll)

    part1 = f'Name: {self.name}\nGender : {self.gender}\nRoll : {self.roll}\nMarks : {self.marks}'

    if self.contactnos:
      part2 = '|'.join(self.contactnos)
    else:
      part2 = 'No contact nos'

    if self.address:
      part3 = '\n' + self.address.getdetails()
    else:
      part3 = '\nNo address'

    return part1 + part2 + part3


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

  # __roll object attribute which is private
  # roll object property which will proxy itself to the __roll attribute (get/set) (public)

  @property
  def roll(self):
    return self.__roll

  @roll.setter
  def roll(self, roll):
    if roll > 0:
      self.__roll = roll
    else:
      self.__roll = None

  @property
  def gender(self):
    return self.__gender

  @gender.setter
  def gender(self, gender):
    if gender == 'm' or gender == 'f':
      self.__gender = gender
    else:
      self.__gender = None


# print(__name__)

# when run the module itself - __main__
# when run as part of import in another module - student

if __name__ == '__main__':
  s1 = Student(name='fatih', gender='f', marks=45, roll=10, contactnos=['86868768'],\
      address=Address('Indian','MH','Mumbai','400053'))
  s1.roll = -100
  s1.gender = 'm'

  s1.gender = 'o'

  s1.gender = 'm'
  s1.roll = 23
  print(s1.getdetails())
  #print(s1.gender)
  #print(s1.roll)
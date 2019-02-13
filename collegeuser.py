# Student IS-A CollegeUser
# Professor IS-A CollegeUser

# super class / Parent class

from address import Address

# object -> built in super class in python lib, that has no super class of its own

# every class in python implicitly inherits from the class object

# Student -> CollegUser (single inheritance)
# Student -> CollegeUser -> object (multilevel inheritance)
class CollegeUser(object):
  def __init__(self, name, gender, contactnos=[], address=None):
    # initializing the common attributes of the sub class object (Student/Professor)
    self.name = name
    self.gender = gender

    if isinstance(contactnos, list):
      self.contactnos = contactnos
    else:
      self.contactnos = []

    if isinstance(address, Address):
      self.address = address
    else:
      self.address = None

  def getdetails(self):
    # self can be Student/Professor/sub class object of CollegeUser
    part1 = f'Name : {self.name}\nGender : {self.gender}\n'

    if self.contactnos:
      part2 = ','.join(self.contactnos)
    else:
      part2 = 'No contact nos'

    if self.address:
      part3 = '\n' + self.address.getdetails()
    else:
      part3 = '\nNo address'

    return part1 + part2 + part3

  # method overriding
  def __str__(self):
    return f'Name: {self.name}\nGender: {self.gender}'

  @property
  def gender(self):
    return self.__gender

  @gender.setter
  def gender(self, gender):
    if gender == 'm' or gender == 'f':
      self.__gender = gender
    else:
      self.__gender = None
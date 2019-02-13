from collegeuser import CollegeUser

# child class / sub class
class Professor(CollegeUser):
  def __init__(self, name, gender, subjects, contactnos=[], address=None):
    # default super call
    # super().__init__()
    # CollegeUser.__init__(self)

    super().__init__(name, gender, contactnos, address)
    # CollegeUser.__init__(self, name, gender, contactnos, address)

    self.subjects = subjects
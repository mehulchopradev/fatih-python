class Address:
  def __init__(self, country, state, city, pincode):
    self.country = country
    self.state = state
    self.city = city
    self.pincode = pincode

  def getdetails(self):
    return f'Country: {self.country}\nState: {self.state}\nCity: {self.city}'
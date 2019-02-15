class Abc:
  def fun(self):
    print('Fun of Abc')

  def hi(self):
    print('Hi from Abc')

class Xyz:
  def fun(self):
    print('Fun of Xyz')

  def hi(self):
    print('Hi of Xyz')

class Mno(Xyz, Abc): # multiple inheritance
  def hi(self):
    # super().hi() # Xyz.hi(self)
    Abc.hi(self)

m = Mno()
m.hi()
m.fun()
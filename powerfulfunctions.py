def abc():
  a = 5 # int object in abc scope
  c = 9 # int object in abc scope

  # nested function definitions

  # function object in abc scope
  def pqr():
    b = 6 # int object in pqr scope
    c = 11 # int objec in pqr scope
    print(b)
    print(a) # access the enclosing function variables (only get)
    print(c) # 11

  pqr()

  print(a)
  print(c) # 9

# abc()
# pqr() # this will not work

# function object in global scope -> mno
def mno(f):
  # f -> mno
  x = 9
  f(x)

# function object in global scope -> xyz
def xyz(y):
  print(y)

mno(xyz) # passing a function as a parameter to another function
# callback functions

def fun(b): # b -> local to fun
  a = 8 # a -> Local to fun

  def inner(): #inner local to fun
    c = 10 + a + b # inner function can get (access) the enclosing functions variables (closure)
    print(c)

  return inner

f1 = fun(5)
f2 = fun(9)

f1()
f2()
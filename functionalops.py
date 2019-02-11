x = 5
# y = x + 2
# z = x + 3

# higher
def incrby(by):
  def increment(ele):
    return ele + by

  return increment

# lower
incrbytwo = incrby(2)
print(incrbytwo(x))
a = 7
print(incrbytwo(a))

incrbyfive = incrby(5)

print(incrbyfive(10))
print(incrbyfive(30))
nos = [5, 6, 3, 4, 10, 7, 8]

# get a new list of only the even nos from nos list
# no for comprehensions
# functional programming

# Common parts of the code
# looping over a list
# while looping, take an element from the list

# dynamic part of the code
# check element for 
  # even
  # odd
  # odd > 5

# higher order functions
def filterFn(elements, fn):
  l = []
  for ele in elements:
    if fn(ele):
      l.append(ele)
  return l

# even nos
def iseven(ele):
  return not ele % 2

evens = filterFn(nos, iseven)
print(evens)

# odd nos greater than 5
def isoddmorethan5(ele):
  return ele % 2 and ele > 5

odds = filterFn(nos, isoddmorethan5)
print(odds)

# get a new list of all the squares from nos list

# Common parts
# creating a list
# for looping on the list
# for every element in the list
# call a function with that element -> mapping value -> append in the list
# return the list

def mapFn(elements, fn):
  l = []
  for ele in elements:
    m = fn(ele)
    l.append(m)

  return l

# squares
def squares(ele):
  return ele ** 2

sq = mapFn(nos, squares)
print(sq)

# squares of even nos cubes of odd numbers
'''def squareevencubeodd(ele):
  return ele ** 3 if ele % 2 else ele ** 2

ans = mapFn(nos, squareevencubeodd)
print(ans)'''

# lower order function should have only one expression
# lambda expression

print(mapFn(nos, lambda ele: ele ** 3 if ele % 2 else ele ** 2))
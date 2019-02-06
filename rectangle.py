def perimeter(length, breadth=2):
  return 2 * (length + breadth)

l = float(input('Enter length : '))
b = float(input('Enter breadth : '))

p = perimeter(l, b)
print(p)

# scope of variables in python is either the function or the entire script file
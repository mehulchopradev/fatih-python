# variable number of arguments
# positional argument packing
def myadd(*args):
  # args becomes an n element tuple
  # print(args)
  return sum(args)

# 0 to n arguments
print(myadd())
print(myadd(4))
print(myadd(4, 5, 9))
print(myadd(4, 5, 9, 10, 5, 3, 5))



# tuple unpacking/ positional arguments unpacking
def perimeter(length, breadth):
  return 2 * (length + breadth)

stats = (5, 3)
# print(perimeter(stats[0], stats[1]))
print(perimeter(*stats))


# keyword argument packing
def area(**stats):
  # print(stats) # stats is a dictionary that has the key word arguments that are passed
  return stats['length'] * stats['breadth']

# print(area(5.3, 5.1)) # this will not work!
print(area(breadth=5.1, length=5.3))
print(area(length=6, breadth=3))


smap = {'length': 7, 'breadth': 3}
# print(perimeter(smap['length'], smap['breadth']))
print(perimeter(**smap)) # dict unpacking



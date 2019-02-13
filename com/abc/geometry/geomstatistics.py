from com.abc.geometry.shape import Shape

def calcstats(shape):
  if isinstance(shape, Shape):
    print(f'Area is {shape.area()}')
    print(f'Perimeter is {shape.perimeter()}')
  else:
    print('Pass in a geometric shape')
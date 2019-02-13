from com.abc.geometry.square import Square
from com.abc.geometry.rectangle import Rectangle
from com.abc.geometry.geomstatistics import calcstats

s1 = Square(5)
# print(s1.area())
# print(s1.perimeter())

r1 = Rectangle(9, 4)

calcstats(s1)
calcstats(r1)


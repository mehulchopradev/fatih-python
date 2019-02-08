nos = [5, 4, 3, 6, 7, 2, 1, 9]

# get a new list from nos, which is only the even elements from nos
# filtering

'''evens = []
for n in nos:
  if not n % 2:
    evens.append(n)

print(evens)'''

# for comprehensions
evens = [n for n in nos if not n % 2]
print(evens)

oddsmorethan5 = [n for n in nos if n % 2 and n > 5]
print(oddsmorethan5)

# get a new list from nos, which is the squares of all elements from nos
# mapping

squares = [n ** 2 for n in nos]
print(squares)

tu = ('mehul', 'jane', 'fatih')
nt = (e for e in tu)
print(nt)
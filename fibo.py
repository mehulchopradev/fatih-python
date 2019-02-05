n = int(input('Enter n : '))

# n -> 8 : 0 1 1 2 3 5 8 13
#          a b c
#            a b c

a, b = 0, 1

print(a)
print(b)

nosleft = n - 2

# Sequence -> 1 - 6 -> 1 - nosleft + 1
for i in range(1, nosleft + 1):
  c = a + b
  print(c)
  a, b = b, c
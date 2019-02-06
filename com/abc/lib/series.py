# Module
# every python script is by default a module
# name -> series

def getfiboseries(n):
  result = ''
  a, b = 0, 1
  result = result + str(a) + '\t' + str(b) + '\t'
  nosleft = n - 2
  for i in range(1, nosleft + 1):
    c = a + b
    result = result + str(c) + '\t'
    a, b = b, c

  return result

def getevenseries(n):
  result = ''
  for i in range(0, n + 1, 2):
    result += str(i) + '\t'
  return result
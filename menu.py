# module
# name -> menu

'''
1. Fiboseries
2. Even Series
3. Even or Odd
4. Exit
Enter ur choice : 1
Enter n : 8
0 1 1 2 3 5 8 13
1. Fiboseries
2. Even Series
3. Even or Odd
4. Exit
Enter ur choice : 2
Enter n : 4
0 2 4
1. Fiboseries
2. Even Series
3. Even or Odd
4. Exit
Enter ur choice : 3
Enter n : 5
Odd
1. Fiboseries
2. Even Series
3. Even or Odd
4. Exit
Enter ur choice : 4
'''
# import series
from com.abc.lib.series import getfiboseries as fiboseries, getevenseries
import com.abc.lib.math as mymath
import math # built in module

# module namespace conflict
# Packages

# method namespace conflict
def getfiboseries(n):
  print('Bla la bla')

while True:
  print('1. Fiboseries\n2. Even Series\n3. Even or Odd\n4. Factorial\n5. Exit')
  choice = int(input('Enter ur choice : '))

  if choice != 5:
    n = int(input('Enter n : '))

  if choice == 1:
    print(fiboseries(n))
    print(getfiboseries(n))
  elif choice == 2:
    print(getevenseries(n))
  elif choice == 3:
    print(mymath.isevenodd(n))
  elif choice == 4:
    print(math.factorial(n))
  else:
    # exit
    break

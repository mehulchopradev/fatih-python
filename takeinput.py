'''print('Program starts')

n = int(input('Enter n : '))
print('Is even') if not n % 2 else print('Is Odd')

print('Program ends')'''

# python env -> takeinput -> int('good morning') -> raises ValueError -> takeinput -> raise ValueError -> python env


# python env -> takeinput -> int('good morning') -> raises ValueError -> takeinput (handle the error)

from traceback import print_exc

print('Program starts')

try:
  n = int(input('Enter n : '))
except ValueError:
  # print('Please enter int value')
  print_exc()
else:
  # which will execute if there is no error thrown in the corresponding try block
  print('Is even') if not n % 2 else print('Is Odd')

print('Program ends')
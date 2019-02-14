from com.abc.bank.account import Account
from traceback import print_exc
from com.abc.bank.insufficientfundserror import InsufficientFundsError

a1 = Account('mehul chopra', 'Savings', 10000)

try:
  ub = a1.withdraw(9000000)
except InsufficientFundsError as e:
  # print_exc()
  print(e)
except ValueError as e:
  print(e)
except TypeError as e:
  print(e)
else:
  print(f'Updated balance after withdrawl is {ub}')

# print(a1.deposit(1000))
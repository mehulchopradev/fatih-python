from com.abc.bank.insufficientfundserror import InsufficientFundsError

class Account:
  minbalance = 1000

  def __init__(self, accname, acctype, accbalance):
    self.accname = accname
    self.acctype = acctype
    self.accbalance = accbalance

  def withdraw(self, amt):
    print('Transaction starts...')

    try:
      if not (isinstance(amt, int) or isinstance(amt, float)):
        raise TypeError('Amt passed in must be float or int')

      if amt <= 0:
        raise ValueError('Amt to be withdrawn must be greater than 0')

      if self.accbalance - amt < Account.minbalance:
        raise InsufficientFundsError('Cannot withdraw. Minimum balance not getting maintained')

      self.accbalance -= amt
      return self.accbalance
    finally:
      # this block executes always irrespective of whether an error is raised in the corresponding try block or no
      print('Transaction ends.')

  def deposit(self, amt):
    self.accbalance += amt
    return self.accbalance
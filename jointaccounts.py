from com.abc.bank.account import Account
from threading import Thread, current_thread, Lock

a = Account('The Simpsons', 'Savings', 10000)

def withdrawaction(a, amt, lock):
  lock.acquire()
  print(f'Balance before withdrawl seen by {current_thread().getName()} is {a.accbalance}')

  try:
    ub = a.withdraw(amt)
    print(f'Balance after withdrawl seen by {current_thread().getName()} is {ub}')
  finally:
    lock.release()
  
lock = Lock() # single lock
husband = Thread(target=withdrawaction, args=(a, 6000, lock), name='Husbandthread')
wife = Thread(target=withdrawaction, args=(a, 5000, lock), name='Wifethread')

husband.start()
wife.start()
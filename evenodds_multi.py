'''
Main thread : Enter n : 
Thread even : Evens till n
Thread odd : Odds till n
'''
from threading import Thread, current_thread

def evennos(n):
  print(f'{current_thread().getName()} is starting execution')
  for i in range(0, n + 1, 2):
    print(i)

def oddnos(n):
  print(f'{current_thread().getName()} is starting execution')
  for i in range(1, n + 1, 2):
    print(i)

print(current_thread().getName()) # MainThread
n = int(input('Enter n : '))

even = Thread(target=evennos, args=(n,), name='EvenThread')
odd = Thread(target=oddnos, args=(n,), name='OddThread')

even.start()
odd.start()

# main thread
even.join()
odd.join()

# these statements from main thread should wait for even and odd thread to finish
print('Even Odd nos printed')
print('Good bye!')
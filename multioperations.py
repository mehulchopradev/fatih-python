'''
Main thread : a, b from the user
Thread add : a + b, print
Thread multiply: a * b, print
'''

from threading import Thread
from time import sleep
import os

def addjob(a, b):
  print(a + b)
  print(os.getpid())

def muljob(a, b):
  sleep(5) # deliberate delay
  print(a * b)
  print(os.getpid())

a = int(input('Enter a : '))
b = int(input('Enter b : '))

addthread = Thread(target=addjob, args=(a, b))
multhread = Thread(target=muljob, args=(a, b))
# multhread.setDaemon(True) # daemonic thread

addthread.start()
multhread.start()

print('Main thread done')

# MainThread runs a non daemon thread
# addthread, multhread run as a non daemon thread
# Python process will be alive if there is minimum 1 non daemon thread alive
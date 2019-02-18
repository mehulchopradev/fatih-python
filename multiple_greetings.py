'''
Thread 1 (main) : Good Morning
           Good Evening
Thread 2 (user defined): Good Afternoon
           Good Night
'''
import threading

def greet_2():
  ''' Job of the thread '''
  print('Good Afternoon')
  print('Good Night')

class Greeterthread(threading.Thread):
  def run(self):
    ''' job of the thread '''
    print('Good Afternoon')
    print('Good Night')

# create a user defined thread
# thread2 = threading.Thread(target=greet_2)
thread2 = Greeterthread()
thread2.start() # schedule the user defined thread for running

# job of the main thread
print('Good Morning')
print('Good Evening')
from os.path import basename
from shutil import copy
from com.abc.lib.series import getfiboseries
from threading import Thread
from time import sleep

def copyfile(sourcefilepath, destfilepath):
  # emulate a long running blocking IO operation
  # deliberate delay
  sleep(15) # pause the execution of the current thread
  copy(sourcefilepath, destfilepath)
  print('Copying done!')

sourcefilepath = input('Enter source file absolute path : ')
destfilepath = f'/Users/mehul.chopra/Desktop/{basename(sourcefilepath)}'

thread = Thread(target=copyfile, args=(sourcefilepath, destfilepath))
thread.start()

series = getfiboseries(50)
print(series)

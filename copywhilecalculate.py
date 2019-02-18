from os.path import basename
from shutil import copy
from com.abc.lib.series import getfiboseries

sourcefilepath = input('Enter source file absolute path : ')
destfilepath = f'/Users/mehul.chopra/Desktop/{basename(sourcefilepath)}'

# IO (Input and Output)
# CPU is free
# Blocking IO operation
copy(sourcefilepath, destfilepath)

# Requires the CPU
series = getfiboseries(50)

print(series)

# Program runs unders a single process
# Under the single process, it run as a single threaded program

# A process can have many threads running under it (Multithreaded program)

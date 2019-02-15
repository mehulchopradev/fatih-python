from os.path import basename
from shutil import copy

sourcefilepath = input('Enter source file absolute path : ')
destfilepath = f'/Users/mehul.chopra/Desktop/{basename(sourcefilepath)}'

copy(sourcefilepath, destfilepath)

'''with open(sourcefilepath, mode='rt') as fs:
  with open(destfilepath, mode='wt') as fd:
    for line in fs:
      fd.write(line)'''

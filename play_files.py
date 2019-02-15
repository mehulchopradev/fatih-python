# filepath = 'menu.py' # relative path
filepath = '/Users/mehul.chopra/Documents/personal/training/fatih/menu.py'

fp = open(filepath, mode='rt') # does not store the whole file in memory
# print(fp)
# print(type(fp))

for line in fp:
  print(line.rstrip()) # removes the trailing \n

print('Trying to read again...')

for line in fp: # it will not go in loop, as file pointer has reached EOF due to above operation
  print(line.rstrip())

print('Another effort to read again...')
fp.seek(0) # takes the file pointer to the start of the file again

for line in fp:
  print(line.rstrip())

# again file pointer has reached the end of file

fp.close() # very imp! Use it once the work is done with the file

# automatic release of resources
filepath = 'address.py'
with open(filepath, mode='rt') as fp:
  for line in fp:
    print(line.rstrip())

  print('Attempting to read address again..')
  fp.seek(0)

  lines = fp.readlines() # reads all the lines together in one burst from the disk to the RAM
  # Note : Do not use this method for reading from large files as u risk an OOM
  # print(len(lines))
  '''for line in lines:
    print(line.rstrip())'''
  # still the file pointer is EOF
  fp.seek(0)

  contents = fp.read() # reads the contents of the entire file in one burst from the disk to the RAM
  # Note : Do not use this method for reading from large files as u risk an OOM
  print(contents)

  # stil the file pointer has reached EOF

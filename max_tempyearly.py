from glob import glob
from fileinput import input

yeartempdict = {}

filepattern = 'data/weather_data_set_*'
files = glob(filepattern)

'''for filepath in files:
  with open(filepath) as fp:
    for line in fp:
      cleanedline = line.rstrip()
      tokens = cleanedline.split('|')

      year = int(tokens[1])
      temperature = float(tokens[4])

      if not year in yeartempdict:
        yeartempdict[year] = temperature
      else:
        if yeartempdict[year] < temperature:
          yeartempdict[year] = temperature

print(yeartempdict)'''

with input(files) as f:
  for line in f:
    cleanedline = line.rstrip()
    tokens = cleanedline.split('|')

    year = int(tokens[1])
    temperature = float(tokens[4])

    if not year in yeartempdict:
      yeartempdict[year] = temperature
    else:
      if yeartempdict[year] < temperature:
        yeartempdict[year] = temperature

print(yeartempdict)




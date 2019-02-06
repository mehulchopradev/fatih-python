from studentops import getdetails, getgrade

# procedural
name = input('Enter name : ')
roll = int(input('Enter roll : '))
gender = input('Enter gender : ')
marks = float(input('Enter marks : '))

print(getdetails(name, gender, roll, marks))
print(getgrade(marks))

# oop object oriented programming
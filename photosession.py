from collegeuser import CollegeUser

def takephoto(collegeuser):
  if isinstance(collegeuser, CollegeUser):
    print(f'Photo taken of {collegeuser.name}')
  else:
    print('Cannot take photo')
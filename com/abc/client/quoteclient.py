from socket import socket

choice = input('Enter a number between 1 and 3')

cs  = socket()
with cs:
  cs.connect(('localhost', 5600))
  cs.send(choice.encode('utf-8'))

  quote = cs.recv(4096).decode('utf-8')
  print(quote)

from socket import socket
from threading import Thread

quotes = ['Quote X', 'Quote Y', 'Quote A']

class ServiceClient(Thread):
  def __init__(self, cs, address):
    super().__init__() # compulsory

    self.cs = cs
    self.address = address

  def run(self):
    cs = self.cs
    # cs I need to recv data
    with cs:
      choice = int(cs.recv(4096).decode('utf-8'))
      quote = quotes[choice-1]
      cs.send(quote.encode('utf-8'))     

portno = 5600

ss = socket()
ss.bind(('', portno))
ss.listen()

while True:
  print('Waiting for client connections...')
  cs, address = ss.accept()
  thread = ServiceClient(cs, address)
  thread.start()
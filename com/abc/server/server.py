# socket
from socket import socket
from datetime import datetime
from threading import Thread
from time import sleep

def serviceclient(cs, address):
  print('Got request from ' + str(address))

  sleep(5) # emulate a long running operation

  # servicing part
  # send back to the client the current date and time
  with cs:
    now = datetime.now()
    datetimestr = now.strftime('%d-%m-%Y %H:%M')
    cs.send(datetimestr.encode('utf-8'))


portno = 6500

ss = socket()
ss.bind(('', portno))
ss.listen()

while True:
  print('Waiting for client connections...')
  cs, address = ss.accept() # blocking method call (Blocking IO call)
  # cs : New socket automatically allocate on server side which can be used to send and receive data
  # from that paricular client
  thread = Thread(target=serviceclient, args=(cs, address))
  thread.start()
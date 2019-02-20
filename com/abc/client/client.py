# socket

from socket import socket

cs = socket()
cs.connect(('localhost', 6500))

data = cs.recv(4096)
print(data.decode('utf-8'))
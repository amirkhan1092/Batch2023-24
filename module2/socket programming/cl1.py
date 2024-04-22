import socket


s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

s.connect(('localhost', 1234))

# data = s.recv(1024)

# print('Data Recieved ', data)
s.send(b'Hello, I am your Client')

s.close()
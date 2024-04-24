# data

import socket
# create the socket 
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

s.connect(('localhost', 9090))

while 1:
    data = input('Client:')
    s.send(data.encode())

    rc = s.recv(1024)
    print('Server:', rc)
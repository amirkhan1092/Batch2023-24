import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

s.bind(('localhost', 1234))


s.listen(1)

print('waiting for connections')
cl, address = s.accept()

# cl.send(b'Welcome to GLA Local Server')
data = cl.recv(1024)
print('Data Recieve From Client', data)
cl.close()

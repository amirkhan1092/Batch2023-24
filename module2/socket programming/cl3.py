import socket


s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)


s.connect(('localhost', 12345))

data = s.recv(1024)

print(data.decode())

s.close()
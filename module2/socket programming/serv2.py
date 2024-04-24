# socket 
import socket
# create the socket 
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

s.bind(('localhost', 9090))
s.listen(1)

print('Waiting for connections ')

client, address = s.accept()

while 1:
    data = client.recv(1024)
    print('Client:', data)

    serv_data = input('Server:').encode()
    client.send(serv_data)



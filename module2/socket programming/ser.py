import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# address = ('localhost', 1234)
address = (socket.gethostname(), 1234)
s.bind(address)
s.listen(1)
print('Waiting for Connections.... address', address)
client, addr = s.accept()
print('Connection Established ', addr)
while 1:
    data = client.recv(1024)
    if not data:
        break
    print('Client:', data)
    data = input('Server: ').encode()
    client.send(data)
    
client.close()
s.close()


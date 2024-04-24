import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

s.bind(('localhost', 12345))

s.listen(1)

print('Waiting for connectin .....')

client, address =  s.accept()

print('Connection Established with', address)
message = 'Welcome to GLA Local Server'.encode()
client.send(message)

s.close()


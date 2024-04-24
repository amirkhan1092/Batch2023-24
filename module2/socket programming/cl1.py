import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

s.connect(('localhost', 1234))
while 1:
    

    message = input('Client:').encode()
    s.send(message)

    data = s.recv(1024)
    print('Server:', data)
    
s.close()






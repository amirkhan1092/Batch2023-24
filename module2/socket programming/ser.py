import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

s.bind(('localhost', 1234))

actual_number = "14"
s.listen(1)

print('waiting for connections')
cl, address = s.accept()
while 1:

    data = cl.recv(1024)
    if data.decode() > actual_number:
        d = "Number is too large try again"
    elif data.decode() < actual_number:
        d = "Number is too small try again!"
    elif data.decode() == actual_number:
        d = "You guessed it correct!"

    print('Client:', data.decode())
    cl.send(d.encode())

cl.close()

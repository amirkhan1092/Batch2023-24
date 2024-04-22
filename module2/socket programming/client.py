import socket

# Create a TCP/IP socket
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect the socket to the server's address and port
server_address = ('localhost', 12346)
client_socket.connect(server_address)

try:
    # Send data
    message = 'Hello, server!'
    print('Sending:', message)
    client_socket.send(message.encode())

    # Receive data
    received_data = b''
    while True:
        data_chunk = client_socket.recv(1024)
        if not data_chunk:
            print('No more data from server')
            break
        received_data += data_chunk

    print('Received:', received_data.decode())

finally:
    # Clean up the connection
    client_socket.close()

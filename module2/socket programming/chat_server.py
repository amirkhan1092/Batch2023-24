import socket
import threading

# Function to handle client connections
def handle_client(client_socket, client_address):
    print(f"Connection from {client_address} established.")

    while True:
        # Receive data from client
        data = client_socket.recv(1024).decode("utf-8")
        if not data:
            break

        print(f"Received from {client_address}: {data}")

        # Echo received data back to client
        client_socket.send(data.encode("utf-8"))

    print(f"Connection from {client_address} closed.")
    client_socket.close()

def main():
    # Create a socket object
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Bind the socket to a specific IP and port
    server_socket.bind(('localhost', 9999))

    # Start listening for incoming connections
    server_socket.listen(5)
    print("Server listening on port 9999...")

    while True:
        # Accept incoming connection
        client_socket, client_address = server_socket.accept()

        # Create a new thread to handle the client
        client_handler = threading.Thread(target=handle_client, args=(client_socket, client_address))
        client_handler.start()

if __name__ == "__main__":
    main()

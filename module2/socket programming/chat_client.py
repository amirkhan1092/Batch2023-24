import socket

def main():
    # Create a socket object
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Connect to the server
    client_socket.connect(('localhost', 9999))

    while True:
        # Send message to server
        message = input("Enter message: ")
        client_socket.send(message.encode("utf-8"))

        # Receive response from server
        response = client_socket.recv(1024).decode("utf-8")
        print("Server:", response)

    # Close the connection
    client_socket.close()

if __name__ == "__main__":
    main()

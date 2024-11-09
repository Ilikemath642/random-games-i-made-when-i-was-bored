import socket
import threading

# Dictionary to store connected clients and their usernames
clients = {}

# Function to handle incoming client messages
def handle_client(client_socket, client_address):
    # Receive username from the client
    username = client_socket.recv(1024).decode('utf-8')
    clients[client_socket] = username
    print(f"{username} from {client_address} has joined the chat.")

    try:
        while True:
            message = client_socket.recv(1024).decode('utf-8')
            if not message:
                break
            # Broadcast the message to all clients
            broadcast_message(f"{username}: {message}", client_socket)
    except:
        print(f"{username} has disconnected.")
    finally:
        client_socket.close()
        del clients[client_socket]
        broadcast_message(f"{username} has left the chat.", client_socket)

# Function to broadcast messages to all clients except the sender
def broadcast_message(message, sender_socket):
    for client in clients:
        if client != sender_socket:
            try:
                client.sendall(message.encode('utf-8'))
            except:
                pass

def main():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    hostname = socket.gethostname()
    server_ip = socket.gethostbyname(hostname)
    server.bind((server_ip, 12345))
    server.listen(5)

    print(f"Server started on IP: {server_ip}, Port: 12345. Waiting for connections...")

    while True:
        client_socket, client_address = server.accept()
        # Start a new thread for each client connection
        threading.Thread(target=handle_client, args=(client_socket, client_address)).start()

if __name__ == "__main__":
    main()

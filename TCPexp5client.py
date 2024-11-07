import socket

# Set up the client
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect(('localhost', 65432))

# Receive and send greetings
server_msg = client_socket.recv(1024).decode()
print(f"Received: {server_msg}")
client_socket.send(b'Hello Server!')

# Receive and save the file
with open('received_file.txt', 'wb') as file:
    file.write(client_socket.recv(1024))

print("File received successfully!")
client_socket.close()

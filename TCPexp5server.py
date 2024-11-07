import socket

# Set up the server
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind(('localhost', 65432))
server_socket.listen(1)

print("Waiting for a connection...")

try:
    # Accept a connection from the client
    conn, addr = server_socket.accept()
    print(f"Connected with {addr}")

    # Send a greeting message to the client
    conn.send(b'Hello Client!')

    # Receive a greeting from the client
    client_msg = conn.recv(1024).decode()
    print(f"Received from client: {client_msg}")

except Exception as e:
    print(f"An error occurred: {e}")
finally:
    # Close the connection
    conn.close()
    server_socket.close()
    print("Connection closed.")

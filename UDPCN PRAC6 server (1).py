import socket
import os

def udp_server():
    # Create a UDP socket
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    server_address = ('localhost', 12345)  # Change to your server's IP and port if necessary
    server_socket.bind(server_address)

    print(f"Server listening on {server_address}...")

    try:
        # First, receive the file name
        print("Waiting to receive file name...")
        file_name, client_address = server_socket.recvfrom(1024)
        file_name = file_name.decode('utf-8').strip()
        print(f"Receiving file: '{file_name}' from {client_address}")

        # Ensure file name is unique to avoid overwriting
        if os.path.exists(file_name):
            file_name = f"new_{file_name}"
            print(f"File already exists. Saving as '{file_name}'.")

        # Now receive the file data
        with open(file_name, 'wb') as f:
            while True:
                print("Waiting for data...")
                data, _ = server_socket.recvfrom(4096)
                if data == b"END":  # Special end marker for end of file transfer
                    print("Received end of file signal.")
                    break
                f.write(data)
                print("Received a chunk of data.")

        print(f"File '{file_name}' received successfully.")
    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        server_socket.close()

if __name__ == "__main__":
    udp_server()

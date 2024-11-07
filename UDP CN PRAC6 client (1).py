import socket
import os

def udp_client(file_path):
    # Create a UDP socket
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    server_address = ('localhost', 12345)  # Change to server's IP and port if necessary

    # Check if the file exists
    if not os.path.exists(file_path):
        print(f"Error: The file '{file_path}' does not exist.")
        return

    # Get the file name from the file path
    file_name = os.path.basename(file_path)

    try:
        # Send the file name first
        client_socket.sendto(file_name.encode('utf-8'), server_address)
        
        # Now send the file data in chunks
        with open(file_path, 'rb') as f:
            while True:
                bytes_read = f.read(4096)  # Read the file in chunks of 4096 bytes
                if not bytes_read:
                    break
                client_socket.sendto(bytes_read, server_address)
        
        # Send an "END" message to indicate the end of the file transfer
        client_socket.sendto(b"END", server_address)
        print(f"File '{file_name}' sent successfully.")
    except Exception as e:
        print(f"An error occurred during file transmission: {e}")
    finally:
        client_socket.close()

if __name__ == "__main__":
    # Replace with the full path of the file you want to send (script, text, audio, video)
    file_path = r"C:\Users\Satchal Patil\CN prac\hi.txt"  # Update to the correct path of your file
    udp_client(file_path)

import os 

# Send a file to the client
def get_file(cli_socket, filename):
    try:
        with open(filename, "rb") as file:
            while (data := file.read(8192)):
                cli_socket.sendall(data)
            cli_socket.sendall(b'EOF')  # Send EOF to signal end of file
            print(f"File '{filename}' sent to client.")
    except Exception as e:
        print(f"Error sending file: {e}")
        cli_socket.sendall(b"Error: Could not send file")

# Receive a file from the client
def recv_file(cli_socket, filename):
    buffer_size = 8192
    try:
        with open(filename, "wb") as file:
            filetype = filename.split(".")
            print(filetype)
            while True:
                data = cli_socket.recv(buffer_size)
                if data == b'EOF':
                    print("End of file transfer reached.")
                    break
                elif not data:
                    print("Connection closed unexpectedly. DATA = ", data)
                    break
                file.write(data)  # Write received data to the file
            print(f"File '{filename}' received successfully.")
    except Exception as e:
        print(f"Error receiving file: {e}")
        cli_socket.sendall(b"Error: Could not receive file")

# Send the listing of files to the client
def send_listing(cli_socket):
    try:
        filename_list = os.listdir()  # Retrieve list of files in directory
        file_list_str = "\n".join(filename_list)
        cli_socket.sendall(file_list_str.encode('utf-8'))
        print("File listing sent to client.")
    except Exception as e:
        print(f"Error sending listing: {e}")
        cli_socket.sendall(b"Error: Could not send file listing")

# Receive and print the directory listing from the server
def recv_listing(cli_socket):
    try:
        data = cli_socket.recv(4096).decode('utf-8')  # Increased buffer size for listings
        print(data)
    except Exception as e:
        print(f"Error receiving listing: {e}")

import socket
import sys
from functions import get_file, recv_file, send_listing

def main():
    host = "0.0.0.0"
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    port = int(sys.argv[1])
    
    try:
        server_socket.bind((host, port))
        server_socket.listen(5)
        print(f"Server up and running on {host}:{port}")

        while True:
            cli_socket, cli_address = server_socket.accept()
            try:
                # Receive the request from the client
                request = cli_socket.recv(1024).decode('utf-8')
                print(f"Received request: {request}")

                #if the user requests put, then we use send_file function
                if request == "put":
                    filename = cli_socket.recv(1024).decode('utf-8')
                    recv_file(cli_socket, filename)
                    print(f"Received the file '{filename}' from {cli_address}")
                #if the user requests get, then we use the recv_file function
                elif request=="get":
                    filename = cli_socket.recv(1024).decode('utf-8')
                    get_file(cli_socket, filename)
                    print(f"Received the file '{filename}' from {cli_address}")
                #if the user requests send_listing we use the send_listing function 
                elif request=="list":
                    send_listing(cli_socket)
                    print(f"Sent file listing to {cli_address}")
                else:
                    print(f"Invalid request received: {request}")
                    cli_socket.send(b"Error: Invalid request format")
            finally:
                cli_socket.close()
    finally:
        server_socket.close()

if __name__ == "__main__":
    main()

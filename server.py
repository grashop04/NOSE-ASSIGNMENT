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
                request = cli_socket.recv(1024).decode('utf-16').strip()
                print(f"Received request: {request}")

                # Split command and filename if present
                parts = request.split(" ", 1)
                command = parts[0]
                filename = parts[1] if len(parts) > 1 else ""

                # Check command type and process accordingly
                if command == "put" and filename:
                    recv_file(cli_socket, filename)
                    print(f"Received the file '{filename}' from {cli_address}")
                elif command == "get" and filename:
                    get_file(cli_socket, filename)
                    print(f"Sent the file '{filename}' to {cli_address}")
                elif command == "list" and not filename:
                    send_listing(cli_socket)
                    print(f"Sent file listing to {cli_address}")
                else:
                    print(f"Invalid request received: {request}")
                    cli_socket.send(b"Error: Invalid request format")
            finally:
                print("about to close cli socket")
                cli_socket.close()
                print("succesfully closed cli socket")
            print("final part of try")
        
    finally:
        print("about to close server socket")
        server_socket.close()
        print("succesfully closed server socket")

if __name__ == "__main__":
    main()

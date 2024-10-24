import socket
import sys
from functions import get_file, recv_file, send_listing
sys.path.append('/Users/callum/Documents/NOSE LAB FILE/NOSE ASSIGNMENT/')

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
                #if the user requests put, then we use send_file function
                if request == "put":
                    recv_file(cli_socket, )
                    print("Received the file")
                    print(cli_address)
                #if the user requests get, then we use the recv_file function
                elif request=="get":
                    get_file(cli_socket)
                    print("Sent the file")
                    print(cli_address)
                #if the user requests send_listing we use the send_listing function 
                elif request=="list":
                    send_listing(cli_socket)
                    print("Sent listing")
                    print(cli_address)
                else:
                    print("Error has occurred, please enter a valid format")
            finally:
                cli_socket.close()
    finally:
        server_socket.close()

if __name__ == "__main__":
    main()

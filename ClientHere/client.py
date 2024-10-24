import sys
import socket 
from functions import get_file, recv_file, recv_listing

def main():
    valid_input = ["put", "get", "list"]

    #validation check 
    if len(sys.argv) < 4 or sys.argv[3] not in valid_input:
        print("Invalid input format")
        return
    
    if sys.argv[3] in ["put", "get"] and len(sys.argv) < 5:
        print(f"Error: Missing filename for '{sys.argv[3]}' request")
        return

    srv_addr = (sys.argv[1], int(sys.argv[2]))
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect(srv_addr)

    try:
        request = sys.argv[3]

        if request=="list":
            sock.send(request.encode('utf-8'))
            recv_listing(sock)
        

        filename = sys.argv[4]
        sock.send(request.encode('utf-8'))
        sock.send(filename.encode('utf-8'))

        if request == "put":
            get_file(sock, filename)
            print("File uploaded successfully")
        elif request =="get":
            recv_file(sock, filename)
            print(f"File '{filename}' downloaded successfully")

        
    except FileNotFoundError:
        print(f"File '{filename}' not found.")
    except IOError as e:
        print(f"Error while sending file: {e}")
    finally:
        sock.close()

if __name__ == "__main__":
    main()

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
        filename = sys.argv[4] if len(sys.argv) > 4 else ""

        request_message = f"{request} {filename}".strip()
        sock.send(request_message.encode('utf-16'))
        print(f"Sent request: {request_message}")


        if request == "list":
            # No need to send a filename for 'list'
            recv_listing(sock)
        elif request == "put":
                get_file(sock, filename)
                print("File uploaded successfully")
        elif request == "get":
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

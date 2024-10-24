
import os 

#get the file
def get_file(cli_socket, filename):
    try:
        with open(filename, "rb") as file:
            data = file.read(1024)
            while data:
                cli_socket.send(data)
                data = file.read(1024)
    except Exception as e:
        print(f"Error sending file: {e}")
    

#recieve file 
def recv_file(cli_socket, filename):
    try:
        with open(filename, "wb") as file:
            while True:
                data = cli_socket.recv(1024)
                file.write(data)
    except Exception as e:
        print(f"Error receiving file: {e}")
      
    
#send listing 
def send_listing(cli_socket):
   try:
   #varibale stores the list directory
    filename_list = os.listdir()
    #string encoded to bytes 
    cli_socket.send(filename_list.encode('utf-8'))
   except Exception as e:
      print(f"something went wrong: {e}")


#recieving the listing
def recv_listing(cli_socket):
    try:
        data = cli_socket.recv(1024).decode
        print( data)
    except Exception as e:
        print(f"Error receiving listing: {e}")
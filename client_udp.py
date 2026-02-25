import socket

SERVER_IP = "127.0.0.1"
PORT = 8821
MAX_MSG_SIZE = 1024

   
my_socket = socket.socket(socket.AF_INET , socket.SOCK_DGRAM)
while True:
    user = input("Please enter your message.")
    my_socket.sendto(user.encode() , (SERVER_IP , PORT))
    (response, remote_address) = my_socket.recvfrom(MAX_MSG_SIZE)
    data = response.decode()
    print( "The server sent " + data)
    if user == "EXIT":
      break

my_socket.close()
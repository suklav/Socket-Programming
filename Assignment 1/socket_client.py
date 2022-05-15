
import socket
host = socket.gethostname()
port = 5000 # socket server port number
client_socket = socket.socket() # creates client side socket
client_socket.connect((host, port)) # connects to the server

msg = client_socket.recv(1024).decode()
print(msg)

message = input(" -> ") # takes input
while message.lower().strip() != 'bye':
    client_socket.send(message.encode()) # sends message
    data = client_socket.recv(1024).decode() # receives response
    print('Received from server: ' + data)
    message = input(" -> ")
client_socket.close() # closes the connection


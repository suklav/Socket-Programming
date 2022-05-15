import socket

print("Server Started...")
host = socket.gethostname()
port = 5000 
server_socket = socket.socket()
server_socket.bind((host, port))
server_socket.listen(2)
conn, address = server_socket.accept()
msg = "Enter filename: "
conn.send(msg.encode())
print("Client connected: " + str(address))
f=''
while True:
    data = conn.recv(1024).decode()
    if not data:
        break
    f+=data
    print("from connected user:" + f)
    try:
      myfile=open(f,"rb")
      conn.send(myfile.read())
    except FileNotFoundError:
      error="Error!file does not exist on the server."
      conn.send(error.encode())
    f=''
conn.close()

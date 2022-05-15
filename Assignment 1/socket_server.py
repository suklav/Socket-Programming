import socket
host = socket.gethostname()
port = 5000 
server_socket = socket.socket()
server_socket.bind((host, port))
server_socket.listen(2)
conn, address = server_socket.accept()
msg = "Enter Principle, rate of interest and year separated by space \n enter bye to disconnect"
conn.send(msg.encode())
print("Connection from: " + str(address))
list = []

while True:
    data = conn.recv(1024).decode()
    if not data:
        break
    s=str(data)
    print("from connected user: " + s)
    list = s.split(" ")
    amt = (float(list[0]) * float(list[1]) * float(list[2])) / 100
    print("The simple interest is:",amt)
    data = str(amt)
    conn.send(data.encode())
conn.close()

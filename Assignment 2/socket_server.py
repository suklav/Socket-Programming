import socket

print("Server Started...")
host = socket.gethostname()
port = 5000 
server_socket = socket.socket()
server_socket.bind((host, port))
server_socket.listen(2)
conn, address = server_socket.accept()
msg = "Message from server: \nEnter operand1,operand2 and operator separated by space \nEnter bye to disconnect"
conn.send(msg.encode())
print("Client connected: " + str(address))
list = []

while True:
    data = conn.recv(1024).decode()
    if not data:
        break
    s=str(data)
    print("from connected user: " + s)
    list = s.split(" ")
    if(len(list)<3):
        print("Invalid Syntax")
        res="Invalid Syntax!"+"\n\n"+msg
        data = str(res)
        conn.send(data.encode())
        continue
    if(list[2]=="+"):
        res=float(list[0])+float(list[1])
        print(res)
    elif(list[2]=="-"):
        res=float(list[0])-float(list[1])
        print(res)
    elif(list[2]=="*"):
        res=float(list[0])*float(list[1])
        print(res)
    elif((list[2]=="/")and (float(list[1])==0)):
        res="Cannot Divide by zero"
        print(res)
    elif((list[2]=="/")and (float(list[1])!=0)):
        res=float(list[0])/float(list[1])
        print(res)
    else:
        res="Invalid Syntax!"+"\n\n"+msg
    data = str(res)
    conn.send(data.encode())
conn.close()

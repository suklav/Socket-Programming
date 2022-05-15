import socket                   

port = 60000                    
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)             
host = socket.gethostname()     
s.bind((host, port))            
s.listen(2)                     

print('Server listening....')

while True:
    conn, addr = s.accept()     
    print('Got connection from', addr)
    data = conn.recv(1024)
    print('Server received: ', data.decode())
    s=str(data.decode())
    list=s.split(" ")
    filename=list[0]
    f = open(filename,'rb')
    block=int(list[1])
    l = f.read(block)
    while (l):
       conn.send(l)
       print('Sent: ',l.decode())
       l = f.read(block)
       if not l:
           break
    f.close()

    print('Done sending')
    break;
conn.close()

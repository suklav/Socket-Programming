import socket

def isprime(num):
    flag=1
    for i in range(2,int(num/2)+1):
        if(num%i==0):
            flag=0
            break
    if(flag==1):
        return 1
    else:
        return 0

def server_program():
    
    host = socket.gethostname()
    port = 60000
    
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)  

    server_socket.bind((host, port))
    
    print("UDP Server Running: ")
    
    string=[]
    while True:
       
        data, address = server_socket.recvfrom(1024)
        
        if not data:
       
            break
        print("from connected user: " + data.decode())
        string=data.decode();
        fstr=""
        for i in range(len(string)):
            if ( isprime(i+1)):
                fstr=fstr+string[i]
        data = fstr;
        server_socket.sendto(data.encode(),address)

    server_socket.close()

if __name__ == '__main__':
    server_program()

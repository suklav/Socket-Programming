import socket                   

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)             
host = socket.gethostname()     
port = 60000                    

s.connect((host, port))
print("Input format : filename,size of the block separated by space")


message = input(" -> ") # takes input
s.send(message.encode())
st=str(message)
ls=[]
ls=st.split(" ")
blk=int(ls[1])
with open('Received_file', 'wb') as f:
    print('File opened')
    while True:
        data = s.recv(blk)
        if not data:
            break
        print('Receiving data...')
        print('Received data: ',data.decode())
        # write data to a file
        f.write(data)
        
f.close()
print('Successfully get the file')
s.close()
print('connection closed')

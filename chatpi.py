import socket
import threading
HOST = '192.168.x.x' #pc的ip地址
PORT = 8001
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  
sock.connect((HOST, PORT))  

<<<<<<< HEAD

<<<<<<< HEAD



=======
>>>>>>> parent of 76ec6eb... Revert "Update chatpi.py"
=======
>>>>>>> parent of b9fe872... Update chatpi.py
def Getdata():
    while True:
        res= sock.recv(1024) 
        print((res).decode())

threading.Thread(target=Getdata).start()




while True:
    se=input()
    if se=='q':
        break 
    sock.send((se).encode("utf-8"))
sock.close() 
print("连接关闭")

import socket
import threading
HOST = '192.168.1.12'        # 连接本地服务器
PORT = 8001               # 设置端口号
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)       # 选择IPv4地址以及TCP协议
sock.bind((HOST, PORT))          # 绑定端口
sock.listen(5)                   # 监听这个端口，可连接最多5个设备

def Getdata():
    while True:
        res= connection.recv(1024) 
        print((res).decode())


while True:  
    connection, address = sock.accept()              # 接受客户端的连接请求
    threading.Thread(target=Getdata).start()
    se=[]
    while True:
        se=input()
        if se=='q':
            break 
        connection.send((se).encode("utf-8"))
    if se=='q':
         break      

   
connection.close() 
print("连接关闭")

import socket
import sys
import os


def echo_server():


    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server_socket.bind(('localhost', 8888))
    server_socket.listen(1)
    print("Echo server is listening on port 8888")

    while True:

        conn, addr = server_socket.accept()
        print(f"Connected by {addr}")
        data = conn.recv(1024).decode()
        if not data:
            conn.close();
	    continue
        print(f"Received: {data}")
        fileResponse = "HTTP/1.1 200 OK\r\n\r\n"
       
        
        try:
            reqFile = data.split(' ')[1]
	    if reqFile = '/':
	    	reqFile = '/index.html'

            f = open(os.getcwd() + reqFile,'r')
            fileData = f.readlines()

            for line in fileData: 
                fileResponse += line
            f.close() 
                    
            conn.sendall((fileResponse + '\r\n').encode())
        except:
            error404 = ("HTTP/1.1 404 Not Found\r\n\r\n".encode())
            conn.sendall(error404)
        
        conn.close()
        print("Connection closed")

echo_server()

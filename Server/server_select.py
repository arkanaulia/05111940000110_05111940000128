import socket
import select
import sys
import os

IP = socket.gethostbyname(socket.gethostname())
PORT = 4455
ADDR = (IP, PORT)
SIZE = 1024
FORMAT = "utf-8"

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
server.bind(ADDR)
server.listen()

input_socket = [server]

try:
    while True:
        read_ready, write_ready, exception = select.select(input_socket, [], [])
        
        for sock in read_ready:
            if sock == server:
                client_socket, client_address = server.accept()
                input_socket.append(client_socket)        
            
            else:            	
                """ Server has accepted the connection from the client. """
                # conn, addr = server.accept()
                print(f"[NEW CONNECTION] {ADDR} connected.")

                """ Receiving the filename from the client. """
                filename = sock.recv(SIZE).decode(FORMAT)
                print(f"[RECV] Receiving the filename.")
                print(filename)
                """file = open(filename, "w")"""
                file_path = "C:/AYO NGODING/Progjar/05111940000110_05111940000128/Server/Dataset/"+ filename
                size = str(os.path.getsize(file_path))
                header = "file-name: "+ filename +",\n"+"file-size: "+ size + ",\n\n\n"
                sock.send(header.encode(FORMAT))
                with open(file_path, "rb") as readfile:
                    while True:
                        # read the bytes from the file
                        bytes_read = readfile.read(1024)
                        sock.sendall(bytes_read)
                        if not bytes_read:
                            print('FILE SENT')
                            break

except KeyboardInterrupt:        
    server.close()
    sys.exit(0)
import socket
import sys
import os

IP = socket.gethostbyname(socket.gethostname())
PORT = 4455
ADDR = (IP, PORT)
SIZE = 1024
FORMAT = "utf-8"

def main():
    print("[STARTING] Server is starting.")
    """ Staring a TCP socket. """
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    """ Bind the IP and PORT to the server. """
    server.bind(ADDR)

    """ Server is listening, i.e., server is now waiting for the client to connected. """
    server.listen()
    print("[LISTENING] Server is listening.")

    try:
        while True:
            """ Server has accepted the connection from the client. """
            conn, addr = server.accept()
            print(f"[NEW CONNECTION] {addr} connected.")

            """ Receiving the filename from the client. """
            filename = conn.recv(SIZE).decode(FORMAT)
            print(f"[RECV] Receiving the filename.")
            print(filename)
            """file = open(filename, "w")"""
            file_path = "C:/Users/ASUS/Documents/Raffi/SEMESTER 6/PROGJAR F/apdet_arkan/Server/Dataset/"+ filename
            size = str(os.path.getsize(file_path))
            header = "file-name: "+ filename +",\n"+"file-size: "+ size + ",\n\n\n"
            conn.send(header.encode(FORMAT))
            with open(file_path, "rb") as readfile:
                while True:
                    # read the bytes from the file
                    bytes_read = readfile.read(1024)
                    if not bytes_read:
                        print('BERES')
                        break
                    conn.sendall(bytes_read)

    except KeyboardInterrupt:        
        server.close()
        sys.exit(0)

if __name__ == "__main__":
    main()
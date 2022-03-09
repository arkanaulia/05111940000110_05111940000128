import socket
import sys

IP = socket.gethostbyname(socket.gethostname())
PORT = 4455
ADDR = (IP, PORT)
FORMAT = "utf-8"
SIZE = 1024

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(ADDR)

sys.stdout.write('>> ')

try:
    while True:

        nama = input("")
        alamat = nama.split()
        """ Sending the filename to the server. """
        client.send(alamat[1].encode(FORMAT))

        print(f"[RECV] Receiving the file data.")

        file_name = alamat[1].strip("\n")
        with open(file_name, "wb") as readfile:
            while True:
                # read 1024 bytes from the socket (receive)
                bytes_read = client.recv(1024)
                # client_socket.settimeout(2)
                if not bytes_read:
                    print('BERES')
                    break
                # write to the file the bytes we just received
                # print(bytes_read)
                readfile.write(bytes_read)

except KeyboardInterrupt:
    client.close()
    sys.exit(0)
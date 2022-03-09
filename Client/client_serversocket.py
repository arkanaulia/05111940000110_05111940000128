import socket
import sys

IP = socket.gethostbyname(socket.gethostname())
PORT = 4455
ADDR = (IP, PORT)
FORMAT = "utf-8"
SIZE = 1024

def main():
    """ Staring a TCP socket. """
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    """ Connecting to the server. """
    client.connect(ADDR)

    """ Opening and reading the file data. """
    """file = open("data/yt.txt", "r")
    data = file.read()"""

    nama = input("")
    alamat = nama.split()
    """ Sending the filename to the server. """
    client.send(alamat[1].encode(FORMAT))
    # msg = client.recv(SIZE).decode(FORMAT)
    # print(f"[SERVER]: {msg}")

    """ Receiving the file data from the server. """
    # data = client.recv(SIZE).decode(FORMAT)
    print(f"[RECV] Receiving the file data.")
    # sys.stdout.write(data)
    file_name = alamat[1].strip("\n")
    with open(file_name, "wb") as readfile:
        while True:
            # read 1024 bytes from the socket (receive)
            bytes_read = client.recv(1024)
            # client_socket.settimeout(2)
            readfile.write(bytes_read)
            if not bytes_read:
                print('BERES')
                break
            # write to the file the bytes we just received
            # print(bytes_read)

    """ Sending the file data to the server. """
    """client.send(data.encode(FORMAT))
    msg = client.recv(SIZE).decode(FORMAT)
    print(f"[SERVER]: {msg}")"""

 


if __name__ == "__main__":
    main()
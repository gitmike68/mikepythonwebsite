# Echo client program
import socket

HOST = '127.0.0.1'    # The remote host
PORT = 2222              # The same port as used by the server
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    command=""
    while command!="close":
        s.sendall(input().encode())
        data = s.recv(1024)
        print('Received ', bytes.decode(data))
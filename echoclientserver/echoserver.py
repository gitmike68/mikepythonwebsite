import socket
import threading

def serv():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind(('127.0.0.1', 2222))
    s.listen(10)

    while True:
        conn, addr = s.accept()
        while True:
            data = conn.recv(1024)
            mes=bytes.decode(data)
            print(mes)
            conn.send(mes.encode())
            if not data or mes=="close":
                break
        conn.close()



def serv10(conn, args):
    while True:
        data = conn.recv(1024)
        mes = bytes.decode(data)
        print(mes)
        if not data or mes == "close":
            break
        conn.send(mes.encode())
    conn.close()

#многопоточный сервер
def conn10():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind(('127.0.0.1', 2222))
    s.listen(10)

    while True:
        conn, addr = s.accept()
        print("Connection", addr)
        t = threading.Thread(target=serv10, nameargs=(conn, addr))
        t.start()
import socket
import threading


def get_client(conn, addr):
    while True:
        msg_len = conn.recv(LEN_MSG).decode(FORMAT)
        if msg_len:
            msg = conn.recv(int(msg_len)).decode(FORMAT)
            send(msg, conn)


def send(msg, conn):
    message = msg.encode(FORMAT)
    msg_len = str(len(message)).encode(FORMAT)
    msg_len += b' ' * (LEN_MSG - len(msg_len))
    for i in connection:
        print(i, conn, bool(i == conn))
        if i != conn:
            i.send(msg_len)
            i.send(message)


IP = socket.gethostbyname(socket.gethostname())
PORTA = 9000
ADDR = (IP, PORTA)

SERVER = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

FORMAT = "utf-8"
LEN_MSG = 64


SERVER.bind(ADDR)
print("[STARTING] Server is Starting ...")
SERVER.listen()

connection = []

while True:
    conn, addr = SERVER.accept()
    print(f"[ACCEPTED] {addr}")
    connection.append(conn)
    threading.Thread(target=get_client, args=(conn, addr)).start()

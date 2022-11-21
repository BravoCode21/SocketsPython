import socket
import threading

HEADER = 64
PORT= 4040
FORMAT="utf-8"
DISCONNET = "DISCONNECT!"
#SERVER="192.168.0.100"
#obtain the ip address automatically by name
SERVER = socket.gethostbyname(socket.gethostname())
ADDR = (SERVER, PORT)

#pick the socket and bind the socket to the IP address

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(ADDR)

def handle_client(conn, addr):
    print(f"New connection {addr} connected ")
    connected = True
    while connected:
        msg_len = conn.recv(HEADER).decode(FORMAT)
        if msg_len:
            msg_len = msg_len
            msg = conn.recv(msg_len).decode(FORMAT)
            print(f"{addr} is {msg}")
            if msg == DISCONNET:
                connected = False

            print(f"the client is {DISCONNET}")

        conn.close()


def start():
    server.listen()
    print(f"the server is listening {SERVER} ")
    while True:
        conn, addr = server.accept()
        thread = threading.Thread(target=handle_client, args=(conn,addr))
        thread.start()
        print(f"ACTIVE CONNECTIONS {threading.activeCount()-1}")

    pass

print('[STARTING THE SERVER]  the server is starting...')
start()






print(SERVER)
print(socket.gethostname())

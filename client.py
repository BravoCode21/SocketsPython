import socket


HEADER = 64
PORT= 4040
FORMAT="utf-8"
DISCONNET = "DISCONNECT!"
SERVER = "192.168.56.1"
ADDR=(SERVER, PORT)

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(ADDR)

def send_msg(msg):
    message = msg.encode(FORMAT)
    msg_len = len(msg)
    send_len = str(msg_len).encode(FORMAT)
    send_len += b''*(HEADER-len(send_len))
    s.send(send_len)
    s.send(message)


send_msg("Hello")


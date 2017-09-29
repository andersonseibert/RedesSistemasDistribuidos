import socket
import uuid
import time
import threading

name = "Galo Cego"
broadcast = "255.255.255.255"
port = 6777
local_id = uuid.uuid4()
announce_interval = 3


# funcao anunciador do usuario
def announcer():
    global local_id
    global name
    global broadcast
    global port
    global announce_interval

    msg = name + ": " + local_id.hex

    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)

    while 1:
        sock.sendto(msg, (broadcast, port))
        time.sleep(announce_interval)


# funcao main
def main():

    thread_announcer = threading.Thread(target=announcer)
    thread_broadcast_listener = threading.Thread(target=broadcast_listener)

    thread_broadcast_listener.start()
    thread_announcer.start()


# funcao escutador
def broadcast_listener():
    global port

    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM, 1)
    sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    sock.bind('0.0.0.0', port)
    sock.listen()

    while True:
        data = sock.recv(1024)
        if not data:
            break

        print data + "\n"


if __name__ == '__main__':
    main()
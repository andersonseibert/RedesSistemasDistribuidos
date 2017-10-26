import uuid
import socket
import json
from time import sleep
from threading import Thread

# broadcast = "192.168.47.255"
# broadcast = "0.0.0.0"
broadcast = "255.255.255.255"
port = 6777
voto_instancia = uuid.uuid4().int

msg = {'remetente': voto_instancia, 'tipo': 0, 'instancia_votada': 0, 'voto_instancia': voto_instancia, 'voto_distribuidor' : voto_instancia}

def sendmessage(msg, repeat):  # ENVIA MENSAGEM
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
    # for i in range(1, repeat):
    while 1:
        sock.sendto(msg, (broadcast, port))
        sleep(0.2)  # intervalo de tempo de envio de pacotes
        print ""+msg


# listener
def broadcast_listener():
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    #sock.bind(broadcast, port)

    while True:
        data = sock.recv(1024)
        if not data:
            break

        print data + "\n"


# funcao main
def main():
    #thread_announcer = Thread(target=sendmessage(""+dados, 4))
    thread_broadcast_listener = Thread(target=broadcast_listener)
    thread_broadcast_listener.start()
    #thread_announcer.start()


if __name__ == '__main__':
    main()

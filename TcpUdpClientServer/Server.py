# -*- coding: utf-8 -*-
import socket, threading


def accept_client():
    while True:
        # accept
        cli_sock, cli_add = ser_sock.accept()
        CONNECTION_LIST.append(cli_sock)
        thread_client = threading.Thread(target=broadcast_usr, args=[cli_sock])
        thread_client.start()
        client_add = cli_sock.getsockname()
        print "HAY >  %s:%s " % client_add


def broadcast_usr(cli_sock):
    while True:
        try:
            data = cli_sock.recv(1024)

            if data:
                b_usr(cli_sock, data)
        except Exception as x:
            print(x.message)
            break


def b_usr(cs_sock, msg):
    for client in CONNECTION_LIST:
        if client != cs_sock:
            client.send(msg)


if __name__ == "__main__":
    CONNECTION_LIST = []

    # socket
    ser_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # bind
    local_addr = ("0.0.0.0", 8000)
    ser_sock.bind(local_addr)

    # listen
    ser_sock.listen(1)
    print('Aguardando conexões: ' + str(""))

    thread_ac = threading.Thread(target=accept_client)
    thread_ac.start()

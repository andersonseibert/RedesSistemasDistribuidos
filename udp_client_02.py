# -*- coding: utf-8  -*-
import socket

remote_addr = ("255.255.255.255", 8000)


def main():
    # criação do socket UDP
    c = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    #Prepara o broadcast
    c.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)

    c.sendto("Aqui é o Anderson", remote_addr)


if __name__ == "__main__":
    main()

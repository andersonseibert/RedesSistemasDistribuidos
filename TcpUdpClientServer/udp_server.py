# -*- coding: utf-8  -*-
import socket

local_addr = ("0.0.0.0", 8000)


def main():
    # criação do socket UDP
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

    # associar o socket a um endereço e porta locais
    # já está pronto para receber
    s.bind(local_addr)
    while 1:

        #aguarda dados
        data, ra = s.recvfrom(256)

        print data


if __name__ == "__main__":
    main()

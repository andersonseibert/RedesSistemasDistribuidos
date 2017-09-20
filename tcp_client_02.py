# -*- coding: utf-8  -*-
import socket


def main():

    #Criação do socket TCP
    c = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # solicita conexão
    c.connect(("127.0.0.1", 8000))

    while 1:
        data = c.recv(256)
        print data
        c.send(raw_input())


if __name__ == "__main__":
        main()

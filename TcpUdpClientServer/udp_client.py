# -*- coding: utf-8  -*-
import socket

remote_addr = ("127.0.0.1", 8000)


def main():
    # criação do socket UDP
    c = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    c.sendto("Aqui é o Anderson", remote_addr)


if __name__ == "__main__":
    main()

# -*- coding: utf-8  -*-
import socket

local_addr = ("0.0.0.0", 8000)


def main():

    # Cria o socket
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

  #  s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEPORT, 1)

    # Associa socket com endereço e porta locais
    s.bind(local_addr)

    # Coloca o socket em escuta
    s.listen(5)

    print "Aguardando conexões em %s:%s" % local_addr


    # Aguarda uma nova conexão
    c, ra = s.accept()

    #Obtém endereço e porta locais
    la = c.getsockname()

    print "Tupla de conexão %s:%s <---> %s:%s" % (la+ra)
    c.send("Sou um servidor de echo!\n ")

    while 1:

        data = c.recv(256)
        data.strip()

        #Enviando informações para o socket
        c.send("Echo: " + data + "!\n")


if __name__ == "__main__":
    main()

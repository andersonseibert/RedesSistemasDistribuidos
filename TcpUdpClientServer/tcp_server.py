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

    while 1:
        # Aguarda uma nova conexão
        c, ra = s.accept()

        #Obtém endereço e porta locais
        la = c.getsockname()

        print "Tupla de conexão %s:%s <---> %s:%s" % (la+ra)

        c.send("Qual é o seu nome? ")
        data = c.recv(256)

        # enviando informações para o socket
        c.send("Tchau " + data + "!\n")

        # fechando o socket
        c.close()


    print "fim"


if __name__ == "__main__":
    main()

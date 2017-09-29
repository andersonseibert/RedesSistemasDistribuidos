# -*- coding: utf-8  -*-
import socket
import threading;

terminate = False


class TCPReader(threading.Thread):
    def __init__(self, client_socket):
        threading.Thread.__init__(self)
        self.socket = client_socket

    def run(self):
        global terminate
        while not terminate:
            try:
                data = self.socket.recv(256)
                print data

            except socket.timeout:
                print "racv timeout"

            except socket.error, e:
                print "socket error: %s" % e
                terminate = True


class KBReader(threading.Thread):
    def __init__(self, client_socket):
        threading.Thread.__init__(self)
        self.socket = client_socket

    def run(self):
        global terminate
        while not terminate:
            line = raw_input().strip()

            if line == "bye":
                terminate = True

            self.socket.send(line.strip())


def main():

    #Criação do socket TCP
    c = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # solicita conexão
    c.connect(("127.0.0.1", 8000))

    c.settimeout(3)
    #c.setblocking(0)

    th1 = TCPReader(c)
    th2 = KBReader(c)

    th1.start()
    th2.start()

    th1.join()
    th2.join()


if __name__ == "__main__":
        main()

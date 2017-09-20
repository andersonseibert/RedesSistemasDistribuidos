import socket


def main():

        s = socket.socket()
        s.bind(('127.0.0.1', 8000))
        s.listen(5)
        c, addr = s.accept()
        print("Usuario " + str(addr) + " se conectou!")
        while True:
            data = c.recv(1024)
            if not data:
                break

            print(str(addr) + " name is " + data.decode("utf-8"))
            # c.send(str.encode(whatever))
        c.close()


if __name__ == "__main__":
    main()

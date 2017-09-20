import socket


def main():

        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect(('127.0.0.1', 8000))
        data = s.recv(256)

        print data

        s.send("Anderson")


if __name__ == "__main__":
        main()

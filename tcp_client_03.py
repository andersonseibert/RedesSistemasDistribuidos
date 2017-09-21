import asyncore, socket


class Client(asyncore.dispatcher):
    #CONTROLA O INICIO DA FUNCAO
    def __init__(self, host, port):
        mensagem = raw_input("Digite alguma coisa: ")
        asyncore.dispatcher.__init__(self)
        self.create_socket(socket.AF_INET, socket.SOCK_STREAM)
        self.connect((host, port))
        self.send(""+mensagem)

    #CONTROLA A LEITURA DA RESPOSTA
    def handle_read(self):
        data = self.recv(1024)
        if data:
            if data == "fechar":
                print "Conexao Finalizada"
                self.close()
                return;

            print "Echo: ", data
            Client('127.0.0.1', 8000)


c = Client('127.0.0.1', 8000)
asyncore.loop()

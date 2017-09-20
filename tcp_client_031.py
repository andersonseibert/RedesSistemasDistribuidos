import asyncore, socket


class Client(asyncore.dispatcher):
    #CONTROLA O INICIO DA FUNCAO
    def __init__(self, host, port):
        asyncore.dispatcher.__init__(self)
        self.create_socket(socket.AF_INET, socket.SOCK_STREAM)
        self.connect((host, port))
        self.send("Roberto")

    #CONTROLA O FIM DA CONEXAO
    def handle_close(self):
        #print "Client: Conexao Fechada"
        self.close()
    #CONTROLA A LEITURA DA RESPOSTA
    def handle_read(self):
        data = self.recv(1024)
        if data:
            print "Recebido do Servidor: ", data


c = Client('127.0.0.1', 8000)
asyncore.loop()

import asyncore, socket


class Server(asyncore.dispatcher):
    #CONTROLA O INICIO DA CLASSE
    def __init__(self, host, port):
        asyncore.dispatcher.__init__(self)
        self.create_socket(socket.AF_INET, socket.SOCK_STREAM)
        self.bind(('', port))
        self.listen(5)
        print "Aguardando por Conexoes..."

    #CONTROLA A ACEITACAO DA CONEXAO
    def handle_accept(self):
        socket, address = self.accept()
        print 'Conexao: ', address
        socket.send(socket.recv(1024))

    #CONTROLA A LEITURA DE DADOS
    def handle_read(self):
        print "Lendo..."
        out_buffer = self.recv(1024)
        if not out_buffer:
            self.close()
        print out_buffer

    #CONTROLA O FECHAMENTO DA CONEXAO
    def handle_closed(self):
        print "Servidor: Conexao Fechada"
        self.close()


s = Server('127.0.0.1', 8000)
asyncore.loop()

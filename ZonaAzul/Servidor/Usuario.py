from Carro import Carro

class Usuario:

    idUsario = ""
    email = ""
    senha = ""
    carro = Carro()
    cpfPessoa = ""
    nome = ""

    def __init__(self):
        pass

    def getidUsuario(self):        
        return self.idUsario

    def setidUsuario(self, id):
        self.idUsario = id

    def getEmail(self):        
        return self.email

    def setEmail(self,mail):
        self.email = mail

    def set(self, senha):
        self.senha = senha

    def getCpf(self):        
        return self.cpfPessoa

    def setCpf(self, cpf):
        self.cpfPessoa = cpf

    def getNome(self):        
        return self.nome

    def setNome(self, nick):
        self.nome = nick

    def getCarro(self):
        return self.carro

    def setCarro(self, car):
        self.carro = Carro
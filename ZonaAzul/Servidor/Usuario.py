from Carro import Carro
class Usuario:

    email = ""
    senha = ""
    user = ""
    carro = Carro()
    cpf = ""
    nome = ""
    login = False
    tempo = 0

    def __init__(self,nome, cpf, email):
        self.nome = nome
        self.cpf = cpf
        self.email = email

    def __repr__(self):
        return "Nome: "+self.nome + ", CPF: " + self.cpf +", Email: " + self.email + ", user: " + self.user + ", Senha: " + self.senha + " Placa: " + self.carro.getPlaca() + " Modelo: " + self.carro.getModelo() + " tempo: " + str(self.tempo)

    def getUser(self):        
        return self.user

    def setUser(self, id):
        self.user = id

    def getEmail(self):        
        return self.email

    def setEmail(self,mail):
        self.email = mail

    def getSenha(self):
        return self.senha

    def setSenha(self, senha):
        self.senha = senha

    def getCpf(self):        
        return self.cpf

    def setCpf(self, cpf):
        self.cpf = cpf

    def getNome(self):        
        return self.nome

    def setNome(self, nick):
        self.nome = nick

    def getCarro(self):
        return "Placa: "+self.carro.getPlaca() + " Modelo: " + self.carro.getModelo()

    def setCarro(self, placa, modelo):
        self.carro = Carro(placa,modelo)

    def getLogin(self):
        return self.login
    
    def setLogin(self, login):
        self.login = login

    def setTempo(self, tempo):
        self.tempo = tempo
    
    def getTempo(self):
        return self.tempo

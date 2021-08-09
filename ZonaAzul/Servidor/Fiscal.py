class Fiscal:

    idFiscal = 0
    cpfPessoa = ""
    nome = ""

    def __init__(self, id, cpf, nome):
        self.idFiscal = id
        self.cpfPessoa = cpf
        self.nome = nome

    def gerarNotificacao(self):
        return 

    def getCpfPessoa(self):
        return self.cpfPessoa

    def setCpfPessoa(self, cpf):
        self.cpfPessoa = cpf
    
    def getNome(self):
        return self.nome
    
    def setNome(self, nome):
        self.nome = nome      
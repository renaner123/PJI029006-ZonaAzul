from servidor.Usuario import Usuario
from servidor.Carro import Carro
from servidor.Aplicacao import Aplicacao

class InterfaceUsuario:

    listUser = dict()
    listUserAuth = []
    aplicacao = Aplicacao()

    def __init__(self):
        pass

    def __repr__(self):
        return str(self.listUser)

    def validaCpf(self, cpf):
        if(cpf in self.listUser):
            return False
        else:
            return True

    def criarConta(self,user, username, password):

        if(self.validaUser(username)):
            user.setUser(username)
            user.setSenha(password)
        else:
            print("Usuario "+ username + " já está em uso")

        if(self.validaCpf(user.getCpf())==False):
            self.listUser[user.getCpf()] = user

    def fazerLogin(self, userAuth, password):
        auxCheck = 0
        auxUser = ""
        for consult in self.listUser:
            if(self.listUser[consult].user == userAuth and self.listUser[consult].senha == password):
                auxCheck = auxCheck + 1
                auxUser = consult
        
        if(auxCheck==1):
            self.listUser[auxUser].login = True
            print("logado")
        else:
            print("Dados inválidos")

    def verificarHistorico(self):
        pass

    def efetuarPagamento(self, user, tempo, vaga):
        if(self.aplicacao.verificarSituacaoVaga(vaga)):
            user.tempo = tempo

    def verificarTempo(self):
        return self.tempo

    def cadastrarVeiculo(self, user, placa, modelo):
        user.setCarro(placa,modelo)

    def getUsuarios(self):
        return self.listUser

    def validaUser(self,username):
        if username not in self.listUserAuth:
            self.listUserAuth.append(username)
            return  True
        else:
            return False

    def validaCpf(self,cpf):
        if(cpf in self.listUser):
            return True
        else:
            return False

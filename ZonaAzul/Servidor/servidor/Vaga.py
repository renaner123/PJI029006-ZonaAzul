from servidor.Carro import Carro

class Vaga:

    idVaga = 0
    idSensor = 0
    status = False
    carro = Carro()
    listVagas = dict()

    listVagas[1] = "vazio"
    listVagas[2] = "vazio"
    listVagas[3] = "vazio"
    listVagas[4] = "vazio"
    listVagas[5] = "vazio"

    def __init__(self):
        pass

    def setIdVaga(self, id):
        self.idVaga = id

    def getIdVaga(self):
        return self.idVaga

    def setIdSensor(self,id):
        self.idSensor = id
    
    def getIdSensor(self):
        return self.idSensor

    def setStatus(self,status):
        self.status = status
    
    def getStatus(self,vaga):
        for x in self.listVagas:
            if(x==vaga):
                if(self.listVagas[x]!="vazio"):
                    return False
        print(self.listVagas)
        return True

    def setCarro(self, carro):
        self.carro = carro
    
    def getCarro(self):
        return self.carro

    def setUsuarioVaga(self,user, vaga):

        for x in self.listVagas:
            if(x==int(vaga)):
                if (self.listVagas[int(vaga)] == "vazio"):
                    self.listVagas[int(vaga)] = user
                else:
                    return False
        return True

    def getVagas(self):
        return self.listVagas

    def getVagaUser(self,user):
        for x in self.listVagas:
            if(self.listVagas[x]==user):
                return x
        return 0


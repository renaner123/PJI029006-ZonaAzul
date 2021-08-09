from Carro import Carro
class Vaga:

    idVaga = 0
    idSensor = 0
    status = ""
    carro = Carro()


    def __init__(self):
        self.idVaga
        self.idSensor
        self.status
        self.carro

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
    
    def getStatus(self):
        return self.status

    def setCarro(self, carro):
        self.carro = carro
    
    def getCarro(self):
        return self.carro


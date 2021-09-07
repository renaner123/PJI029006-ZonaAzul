from servidor.Carro import Carro

class Vaga:

    idVaga = 0
    idSensor = 0
    status = False
    tempo = 0
    tempoDatatime = 0

    def __init__(self, idVaga, idSensor):
        self.idVaga = idVaga
        self.idSensor = idSensor

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

    def setTempo(self, tempo):
        self.tempo = tempo

    def getTempo(self):
        return self.tempo

    def setDatatime(self,data):
        self.tempoDatatime = data

    def getDatatime(self):
        return self.tempoDatatime

class Aplicacao:

    VALORHORA = 2
    VALORFRACAO = 1
    
    usuario = []
    fiscais = []
    totem = []
    vagas = dict()
    idServidor = 0 

    def __init__(self):
        pass

    def verificarSituacaoVaga(self, idVaga):
        if(self.sendToTotem(idVaga)):
            return True

    def confirmarSituacaoVaga(self, idVaga, status):
        self.sendToTotem(idVaga, status)
        
    def cadastrarVaga(self, idVaga, idSensor):
        self.vagas[idVaga] = idSensor

    def sendToTotem(self, comando, **argv):
        return True
    
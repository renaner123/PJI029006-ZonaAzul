class Carro:

    placa = ""
    modelo = ""

    def __init__(self, placa="", modelo=""):
        self.placa = placa
        self.modelo = modelo

    def __str__(self):
        return 'Placa: {} Modelo: {}'.format(self.placa, self.modelo)

    def __repr__(self):
        return 'Placa: {} Modelo: {}'.format(self.placa, self.modelo)
    def getPlaca(self):
        return self.placa

    def setPlaca(self, placa):
        self.placa = placa

    def getModelo(self):
        return self.modelo
    
    def setModelo(self, modelo):
        self.modelo = modelo
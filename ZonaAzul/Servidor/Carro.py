class Carro:

    placa = ""
    modelo = ""

    def __init__(self, placa="", modelo=""):
        self.placa = placa
        self.modelo = modelo

    def __repr__(self):
         return "Placa: ", self.placa + ", Modelo: " + self.modelo        

    def getPlaca(self):
        return self.placa

    def setPlaca(self, placa):
        self.placa = placa

    def getModelo(self):
        return self.modelo
    
    def setModelo(self, modelo):
        self.modelo = modelo
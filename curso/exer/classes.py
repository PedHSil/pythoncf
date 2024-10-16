class Carro:
    def __init__(self, nome):
        self.nome = nome
        self.motor = None
        self.fabricante = None
        
    @property
    def motor(self):
        return self.__motor
    
    @motor.setter
    def motor(self, valor):
        self.__motor = valor
      
    @property
    def fabricante(self):
        return self.__fabricante
    
    @fabricante.setter
    def fabricante(self, valor):
        self.__fabricante = valor
          
class Motor:
    def __init__(self, nome):
        self.nome = nome
        
class Fabricante:
    def __init__(self, nome):
        self.nome = nome
        
        
yaris = Carro('Yaris')
toyota = Fabricante('Toyota')
motor = Motor('1.6 4 cilindros em linha turbo')
yaris.fabricante = toyota
yaris.motor = motor
print(yaris.nome, yaris.fabricante.nome, yaris.motor.nome)

corolagr = Carro('Corolla GR')
toyota = Fabricante('Toyota')
motor = Motor('1.6 6 cilindros em linha turbo')
corolagr.fabricante = toyota
corolagr.motor = motor
print(corolagr.nome, corolagr.fabricante.nome, corolagr.motor.nome)

raptor = Carro('Raptor')
toyota = Fabricante('Ford')
motor = Motor('v8 bi-turbo 5l combustível')
raptor.fabricante = toyota
raptor.motor = motor
print(raptor.nome, raptor.fabricante.nome, raptor.motor.nome)
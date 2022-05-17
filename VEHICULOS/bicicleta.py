from vehiculo import Vehiculo 

class Bicicleta(Vehiculo):

    def __init__(self,tipo,color):
        self.tipo = tipo

        Vehiculo.__init__(self,color,ruedas=2)


    def __str__(self):
        return f"{type(self).__name__},{self.tipo},{self.color},{self.ruedas}"  
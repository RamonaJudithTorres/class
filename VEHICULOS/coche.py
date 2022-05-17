from vehiculo import Vehiculo 

class Coche(Vehiculo):

    def __init__(self,velocidad, cilindrada, color):
        self.velocidad= velocidad
        self.cilindrada= cilindrada

        Vehiculo.__init__(self,color,ruedas=4)

    
    def __str__(self):
        return f"{type(self).__name__},{self.velocidad},{self.cilindrada},{self.color},{self.ruedas}"    


    

    








from bicicleta import Bicicleta


class Motocicleta(Bicicleta):
    def __init__(self,velocidad,cilindrada,tipo,color):
        self.cilindrada= cilindrada
        self.velocidad =velocidad

        Bicicleta.__init__(self,tipo,color)
    
        

    
    def __str__(self):
        return f"{type(self).__name__},{self.velocidad},{self.cilindrada},{self.tipo},{self.color},{self.ruedas}"

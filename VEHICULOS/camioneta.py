from coche import Coche

class Camioneta(Coche):
    def __init__(self,velocidad, cilindrada, color, carga):
        self.carga =carga

        Coche.__init__(self,velocidad, cilindrada, color)


    def __str__(self):
        return f"{type(self).__name__},{self.velocidad},{self.cilindrada},{self.color},{self.carga},{self.ruedas}" 









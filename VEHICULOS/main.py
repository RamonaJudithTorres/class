from coche import Coche
from camioneta import Camioneta
from bicicleta import Bicicleta
from motocicleta import Motocicleta


def catalogar(vehiculos,ruedas):
    print (vehiculos)       
    for i in vehiculos:
        if i.ruedas==2:
            print (i)


if __name__ == "__main__":  
    coche1 = Coche(190,1500,"rojo")
    coche2 = Coche(160,2500,"amarillo")
    camioneta1=Camioneta(200,3000,"negro",500)
    camioneta2=Camioneta(200,3000,"verde",1200)
    bicicleta1=Bicicleta("urbana","verde")
    bicicleta2=Bicicleta("deportiva","celeste")
    motocicleta1 = Motocicleta(160,1500,"urbana","azul")
    motocicleta2 = Motocicleta(160,1500,"deportiva","negro")

    vehiculos=[coche1,coche2,camioneta1,camioneta2,bicicleta1,bicicleta2,motocicleta1,motocicleta2] 
    catalogar(vehiculos)







"""Realiza una función llamada catalogar() que reciba la lista de vehiculos y 
los recorra mostrando el nombre de su clase y sus atributos"""






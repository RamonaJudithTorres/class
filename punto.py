class Punto :
    def __init__(self,x=0,y=0):
        self.x=x
        self.y=y


    def __str__(self):
        return f"{self.x},{self.y}"



    def cuadrante(self):
        if self.x==0 and self.y!=0:
            print("Eje Y")
        if self.x!=0 and self.y==0:
            print("Eje X")
        if self.x==0 and self.y==0:
            print("Origen")    
        if self.x>0 and self.y>0 :
            print("Cuadrante I")  
        if self.x<0 and self.y>0 :
            print("Cuadrante II") 
        if self.x<0 and self.y<0 :
            print("Cuadrante III") 
        if self.x>0 and self.y<0 :
            print("Cuadrante IV")  
    

    def vector(self, punto):
        
        print(f"El vector es : { punto.x- self.x} {punto.y- self.y}")
    
    def distancia(self,punto):
        dist=  (abs( ((punto.y-self.y)**2) - ((punto.x-self.x)**2) ))**.5
        print (f"La distancia entre los puntos es: {dist} ")



    
  
    
       




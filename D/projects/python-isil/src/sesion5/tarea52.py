#https://github.com/YFRM/python-isil
from tarea51 import Punto
class Triangulo(Punto):

    def perimetro(self):
        print("Mis coordenadas son :",self.x2,self.x1,self.y2,self.y1)
        return (self.x2+self.x1+self.y2+self.y1)

obj = Triangulo(1,1,3,5)
print ('El perimetro es: ', obj.perimetro())
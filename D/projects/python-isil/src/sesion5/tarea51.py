#https://github.com/YFRM/python-isil
class Punto():
    def __init__(self, x2, x1, y2, y1):
        self.x2 = x2
        self.x1 = x1
        self.y2 = y2
        self.y1 = y1
    def distancia(self):
        print("Mis coordenadas son :",self.x2,self.x1,self.y2,self.y1)
        return self.x2-self.x1*2+self.y2-self.y1*2
def  principal():
    obj = Punto(10,0,0,0)
    print ('La Distancia entre los puntos es: ', obj.distancia())

if __name__ == '__main__':
     principal()


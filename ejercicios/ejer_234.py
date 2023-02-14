class Punto:
    def __init__(self,x,y):
        self.x: int = x
        self.y: int = y

    def coordenadas(self,x,y):
        print(self.x,self.y)

    def mover(self,nuevo_x,nuevo_y):
        self.x = nuevo_x
        self.y = nuevo_y

    def calcular_distancia(self, nuevo_x,nuevo_y,x,y):
        return (((nuevo_x-x)**2)+(nuevo_y-y)**2)**0.5


class Rectangulo:
    def __init__(self,punto_1,punto_2):
        self.punto_1: Punto = punto_1
        self.punto_2: Punto = punto_2

    def area(self)->float:
        base = abs(self.punto_2.x - self.punto_1.x)
        altura = abs(self.punto_2.y - self.punto_1.y)
        return base*altura

    def perimetro(self)->float:
        base = abs(self.punto_2.x - self.punto_1.x)
        altura = abs(self.punto_2.y - self.punto_1.y)
        return (base+base)*(altura+altura)

    def es_cuadrado(self)->bool:
        base = abs(self.punto_2.x - self.punto_1.x)
        altura = abs(self.punto_2.y - self.punto_1.y)
        return base==altura
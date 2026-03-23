import math

class Vector:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def __add__(self, otro):
        return Vector(self.x + otro.x, self.y + otro.y, self.z + otro.z)

    def __sub__(self, otro):
        return Vector(self.x - otro.x, self.y - otro.y, self.z - otro.z)

    def __mul__(self, r):
        return Vector(self.x * r, self.y * r, self.z * r)

    def longitud(self):
        return math.sqrt(self.x**2 + self.y**2 + self.z**2)

    def normal(self):
        m = self.longitud()
        if m == 0: return Vector(0, 0, 0)
        return Vector(self.x / m, self.y / m, self.z / m)

    def productoP(self, otro):
        return (self.x * otro.x) + (self.y * otro.y) + (self.z * otro.z)

    def __str__(self):
        return f"({self.x}, {self.y}, {self.z})"



class AlgebraVectorial:
    k = 1e-6 
    @staticmethod
    def perpendicularDiag(a, b):
        suma = (a + b).longitud()
        resta = (a - b).longitud()
        return abs(suma - resta) < AlgebraVectorial.k 

    @staticmethod 
    def proyeccion(a, b):
        x = a.productoP(b)
        y = b.longitud()**2
        escalar = x / y
        return b * escalar 

    @staticmethod
    def componente(a, b):
        return a.productoP(b) / b.longitud()

class Main:

    v1 = Vector(3, 0, 0)
    v2 = Vector(0, 4, 0)
    
    perp = AlgebraVectorial.perpendicularDiag(v1, v2)
    print(f"PerpendicularDiag: {perp}")
    
    a = Vector(2, 3, 0)
    b = Vector(5, 0, 0)
    
    print(f"Vector a: {a} sobre Vector b: {b}")
    print(f"proyección : {AlgebraVectorial.proyeccion(a, b)}")
    print(f"componente : {AlgebraVectorial.componente(a, b)}")
    print(f"\nVector a normal: {a.normal()}")

if __name__ == "__main__":
    Main()
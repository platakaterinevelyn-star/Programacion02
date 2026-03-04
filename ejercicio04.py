#orientada a objetos EJERCICIO 4#
class Estadistica():
    n=None
    edades=[]
    suma=0

    def leer(self):
        self.n=int(input("estudiantes:"))
        for i in range (self.n):
            self.edades.append(float(input("edades:")))
            self.suma= self.edades[i] + self.suma
        return (self.suma)
    
    def promedio(self):
        X= self.suma / self.n 
        print(X)
        return (X)
       

    def desviacion(self):
        Z=self.promedio()
        import math 
        K=0
        for i in range (self.n):
           K=((self.edades[i] - Z)**2) + K
        Y= math.sqrt(K / (self.n - 1))
        print(Y)

d=Estadistica()
d.leer()
d.promedio()
d.desviacion()



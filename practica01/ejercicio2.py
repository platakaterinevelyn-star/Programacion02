class Ecuacion_lineal():
    
    def __init__(self):
        self.__a=float(input("a:"))
        self.__b=float(input("b:"))
        self.__c=float(input("c:"))
        self.__d=float(input("d:"))
        self.__e=float(input("e:"))
        self.__f=float(input("f:"))
        
    def tiene_solucion(self):
        if (((self.__a * self.__d) - (self.__b * self.__c)) !=0):
            print ("Tiene solucion")
            return True
        else:
            print("No tiene solucion")
            return False
        
    def getX(self):
        X=((self.__e * self.__d) - (self.__b * self.__f)) /  ((self.__a * self.__d) - (self.__b * self.__c) )
        print (X)

    def getY(self):
        Y=((self.__a * self.__f) - (self.__e * self.__c)) /  ((self.__a * self.__d) - (self.__b * self.__c) )
        print (Y)

d=Ecuacion_lineal()
d.tiene_solucion()
d.getX()
d.getY()



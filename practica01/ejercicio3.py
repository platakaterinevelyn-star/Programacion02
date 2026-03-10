class Ecuacion_lineal():

    def __init__(self):
        self.__a=float(input("a:"))
        self.__b=float(input("b:"))
        self.__c=float(input("c:"))

    def getDiscriminante(self):
        X=(self.__b)**2 - (4 * self.__a * self.__c)
        return (X)

    def getRaiz1(self):
        import math
        r1= (- (self.__b) + math.sqrt((self.__b)**2 - (4 * self.__a * self.__c))) / (2 * self.__a)
        print(r1)

    def getRaiz2(self):
        import math
        r2= (- (self.__b) - math.sqrt((self.__b)**2 - (4 * self.__a * self.__c))) / (2 * self.__a)
        print(r2)
        
d=Ecuacion_lineal()
di= d.getDiscriminante()
if (di)>0 :
    d.getRaiz1()
    d.getRaiz2()

elif(di==0):
    d.getRaiz2()

else:
    print("La ecuacion no tiene raices Reales")


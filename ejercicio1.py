import time
import random
class Cronometro:

    def __init__(self):
        self.__inicia= int(time.time()* 1000)
        self.__finalizar= None

    def getInicia(self):
        return self.__inicia
    
    def getFnaliza(self):
        return self.__finalizar
    
    def inicia(self):
        self.__inicia=int(time.time()* 1000)
        self.__finalizar= None
    
    def detener(self):
        self.__finalizar=int(time.time()* 1000)

    def LapsodeTiempo(self):
        if self.__finalizar is None:
            return None
        return self.__finalizar - self.__inicia 
    
class Main():
    vect = []

    for i in range(100000):
        vect.append(random.randint(1,100000))

    def seleccion_sort(lista):
        n= len(lista)
        for i in range(n):
            min = i
            for j in range(i+1, n):
                if lista[j] < lista[min]:
                    min=j
            lista[i], lista[min]= lista[min], lista[i]
        return lista
    d= Cronometro()
    d.inicia()
    vect02 = seleccion_sort(vect)
    d.detener()
    print(f"lapzo de tiempo: {d.LapsodeTiempo()}ms")


   





    



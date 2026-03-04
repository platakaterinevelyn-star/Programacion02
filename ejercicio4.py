#metodo estructurado EJERCICIO 4#
def leer(n):
    edades=[]
    suma=0
    for i in range (n):
            edades.append(float(input("edades:")))
            suma= edades[i] + suma
    return (suma,edades)
    
def promedio(n,suma):
        X= suma / n 
        print(X)
        return (X)


def desviacion(n,promedio,edades):
        Z=promedio(n,suma)
        import math 
        K=0
        for i in range (n):
           K=((edades[i] - Z)**2) + K
        Y= math.sqrt(K / (n - 1))
        print(Y)
        return(Y)


n=int(input("estudiantes:"))
suma,edades=leer(n)
prom=promedio(n,suma)
des=desviacion(n,promedio,edades)



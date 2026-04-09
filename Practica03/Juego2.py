import random

class Juego2():
    def __init__(self, numeroDeVidas):
        self.numeroDeVidas = numeroDeVidas
        self.record = 0
        self.vidasIniciales = numeroDeVidas
    
    def reiniciaPartida(self):
        self.numeroDeVidas = self.vidasIniciales
        print("partida reiniciada")

    def actualizarRecord(self):
        self.record = self.record + 1
        
    def quitaVida(self):
        self.numeroDeVidas = self.numeroDeVidas - 1
        if self.numeroDeVidas > 0:
            return True
        else:
            return False

class JuegoAdivinaNumero(Juego2):
    def __init__(self, numeroDeVidas):
        super().__init__(numeroDeVidas)
        self.numeroAAdivinar = 0
        
    def validaNumero(self, numero):
        if numero >= 0 and numero <= 10:
            return True
        print("ERROR: numero entre 0 y 10")
        return False
    
    def juega(self):
        self.reiniciaPartida()
        self.numeroAAdivinar = random.randint(0, 10)
        print("Adivinar nro entre el 0 y 10")
        
        while True:  
            numero = int(input("numero:"))
            
            if not self.validaNumero(numero):
                continue
            
            if numero == self.numeroAAdivinar:
                print("Acertaste!!")
                self.actualizarRecord()
                break
            else: 
                if self.quitaVida():                  
                    if numero < self.numeroAAdivinar:
                        print("El numero es mayor")
                    else:
                        print("El numero es menor")
                else: 
                    print(f"sin vida era {self.numeroAAdivinar}")                           
                    break

class JuegoAdivinaPar(JuegoAdivinaNumero):
    
    def validaNumero(self, numero):
        if super().validaNumero(numero):
            if numero % 2 == 0:
                return True
            print("Error solo pares")
            return False
        return False
    
    def juega(self):
        self.reiniciaPartida()
        self.numeroAAdivinar = random.randrange(0, 11, 2)
        print("Adivinar nro entre el 0 y 10")
        
        while True:  
            numero = int(input("numero:"))
            
            if not self.validaNumero(numero):
                continue
            
            if numero == self.numeroAAdivinar:
                print("Acertaste!!")
                self.actualizarRecord()
                break
            else: 
                if self.quitaVida():                  
                    if numero < self.numeroAAdivinar:
                        print("El numero es mayor")
                    else:
                        print("El numero es menor")
                else: 
                    print(f"sin vida era {self.numeroAAdivinar}")                           
                    break
    
class JuegoAdivinaImpar(JuegoAdivinaNumero):
    
    def validaNumero(self, numero):
        if super().validaNumero(numero):
            if numero %  2 !=0 :
                return True
            print("Error solo impares")
            return False
        return False
    
    def juega(self):
        self.reiniciaPartida()
        self.numeroAAdivinar = random.randrange(1, 10, 2)
        print("Adivinar nro entre el 0 y 10")
        
        while True:  
            numero = int(input("numero:"))
            
            if not self.validaNumero(numero):
                continue
            
            if numero == self.numeroAAdivinar:
                print("Acertaste!!")
                self.actualizarRecord()
                break
            else: 
                if self.quitaVida():                  
                    if numero < self.numeroAAdivinar:
                        print("El numero es mayor")
                    else:
                        print("El numero es menor")
                else: 
                    print(f"sin vida era {self.numeroAAdivinar}")                           
                    break

class Aplicacion:
    def main(self):
        print("--NUMEROS NORMALES--")
        d = JuegoAdivinaNumero(3)
        d.juega()
        
        print("--NUMEROS PARES--")
        p = JuegoAdivinaPar(3)
        p.juega()
        
        print("--NUMEROS IMPARES--")
        im = JuegoAdivinaImpar(3)
        im.juega()

Aplicacion().main()




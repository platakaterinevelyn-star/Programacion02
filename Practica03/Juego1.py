import random
class Juego1():
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
        
class JuegoAdivinaNumero(Juego1):
    def __init__(self, numeroDeVidas):
        super().__init__(numeroDeVidas)
        self.numeroAAdivinar = 0

    def juega(self):
        self.reiniciaPartida()
        self.numeroAAdivinar = random.randint(0, 10)
        print("Adivinar nro entre el 0 y 10")
        while True:  
            numero = int(input ("numero:"))
         
            if numero == self.numeroAAdivinar:
                print("Acertaste!!")
                self.actualizarRecord()
                break
            else: 
                if  self.quitaVida():                  
                    if numero < self.numeroAAdivinar:
                        print("El numero es mayor")
                    else:
                        print("El numero es menor")
                else: 
                    print(f"sin vida era {self.numeroAAdivinar}")  
                    break                           
                    
class Aplicacion:
    def main(self):
        d= JuegoAdivinaNumero(3)
        d.juega()
Aplicacion().main()
import random
class Juego:
    def __init__(self,lanzamientos,jugador):
        self.lanzamientos = lanzamientos
        self.jugador = jugador
        
    def dado(self):
        resultado = random.randint(1,6)
        return resultado
    def suma_resta(self):
        contador = 0
        puntaje = 0
        while contador <= self.lanzamientos:
            tiro = self.dado()
            if contador % 2 ==0:
                puntaje += tiro
            else:
                puntaje -= tiro
            contador +=1
        return puntaje
    def __str__(self):
        resultado = self.suma_resta()
        cadena = "El jugador "+ self.jugador + " ha obtenido "+ str(resultado)+" puntos"
        return cadena

jugador1 = Juego(10,"pablo")
jugador1.dado()
jugador1.suma_resta()
print(jugador1)



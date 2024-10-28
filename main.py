import random

puntuacion = 0
vidas = 3

def inicializarJuego():
    print("--------------------------------------------------")
    print(" BIENVENIDO AL JUEGO DE LAS TABLAS DE MULTIPLICAR")
    print(" VIDAS DISPONIBLES: ", vidas,)
    print("--------------------------------------------------")

def preguntar_aleatorio():
    primer_operando = random.randint(0,10)
    segundo_operando = random.randint(0,10)
    return primer_operando, segundo_operando

def solucionar(primer_operando, segundo_operando, respuesta):
    if (primer_operando * segundo_operando == respuesta):
        return 'ganador'
    return 'perdedor'

def ganador(puntuacion):
    print("\n¡Correcto!")
    puntuacion += 1
    return puntuacion

def perdedor(vidas):
    print("\n¡Incorrecto!")
    vidas -= 1
    return vidas

# INICIO PROGRAMA

inicializarJuego()
while(vidas != 0):
    primer_operando, segundo_operando = preguntar_aleatorio()
    print("PREGUNTA: ", primer_operando, "x", segundo_operando, sep="")
    respuesta = int(input("Respuesta: "))
    solucion = solucionar(primer_operando, segundo_operando, respuesta)
    if (solucion == 'ganador'):
        puntuacion = ganador(puntuacion)
    else:
        vidas = perdedor(vidas)
    print("\nPuntuación:", puntuacion, "\nVidas restantes:", vidas, "\n")

print("RESULTADO FINAL:", puntuacion)
print("¡Gracias por jugar!")
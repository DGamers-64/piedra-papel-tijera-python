import random

puntuacion = 0
vidas = 3

def inicializarJuego():
    print("--------------------------------------------------")
    print(" BIENVENIDO AL JUEGO DE LAS TABLAS DE MULTIPLICAR")
    print(" VIDAS RESTANTES: ", vidas,)
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
    print("¡Correcto!")
    puntuacion += 1
    print(puntuacion)
    return

def perdedor(vidas):
    print("¡Incorrecto")
    vidas -= 1
    print(vidas)

# INICIO PROGRAMA

inicializarJuego()
primer_operando, segundo_operando = preguntar_aleatorio()
print("PREGUNTA: ", primer_operando, "x", segundo_operando, sep="")
respuesta = int(input("Respuesta: "))
solucion = solucionar(primer_operando, segundo_operando, respuesta)
print(solucion)

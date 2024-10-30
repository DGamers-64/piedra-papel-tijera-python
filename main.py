import random

def inicializarJuego():
    print("--------------------------------------------------")
    print(" BIENVENIDO AL JUEGO DE LAS TABLAS DE MULTIPLICAR")
    print(" VIDAS DISPONIBLES: ", vidas,)
    print("--------------------------------------------------")
    print(" ELIGE UNA DIFICULTAD:")
    print("     1. Fácil")
    print("     2. Intermedio")
    print("     3. Difícil")
    dificultad = int(input(" Introduce un número: "))
    print("--------------------------------------------------")
    return dificultad
    
def preguntar_aleatorio():
    primer_operando = random.randint(0,10)
    segundo_operando = random.randint(0,10)
    return primer_operando, segundo_operando

def solucionar(primer_operando, segundo_operando, operando, respuesta):
    match operando:
        case 1:
            return primer_operando + segundo_operando == respuesta
        case 2:
            return primer_operando - segundo_operando == respuesta
        case 3:
            return primer_operando * segundo_operando == respuesta
        case _:
            return False

def ganador(puntuacion):
    print("\n¡Correcto!")
    puntuacion += 1
    return puntuacion

def perdedor(vidas):
    print("\n¡Incorrecto!")
    vidas -= 1
    return vidas

def facil(puntuacion, vidas):
    while(vidas != 0):
        primer_operando, segundo_operando = preguntar_aleatorio()
        print("PREGUNTA: ", primer_operando, "x", segundo_operando, sep="")
        respuesta = int(input("Respuesta: "))
        solucion = solucionar(primer_operando, segundo_operando, 3, respuesta)
        if (solucion):
            puntuacion = ganador(puntuacion)
        else:
            vidas = perdedor(vidas)
        print("\nPuntuación:", puntuacion, "\nVidas restantes:", vidas, "\n")
    return puntuacion

def intermedio(puntuacion, vidas):
    while(vidas != 0):
        operando = random.randint(1,3)
        match operando:
            case 1:
                simbolo_operando = '+'
            case 2:
                simbolo_operando = '-'
            case 3:
                simbolo_operando = 'x'
        primer_operando, segundo_operando = preguntar_aleatorio()
        print("PREGUNTA: ", primer_operando, simbolo_operando, segundo_operando, sep="")
        respuesta = int(input("Respuesta: "))
        solucion = solucionar(primer_operando, segundo_operando, operando, respuesta)
        if (solucion):
            puntuacion = ganador(puntuacion)
        else:
            vidas = perdedor(vidas)
        print("\nPuntuación:", puntuacion, "\nVidas restantes:", vidas, "\n")
    return puntuacion

# def dificil(puntuacion, vidas):


    # while(vidas != 0):
    #     operando = random.randint(1,3)
    #     match operando:
    #         case 1:
    #             simbolo_operando = '+'
    #         case 2:
    #             simbolo_operando = '-'
    #         case 3:
    #             simbolo_operando = '*'
    #     primer_operando, segundo_operando = preguntar_aleatorio()
    #     print("PREGUNTA: ", primer_operando, simbolo_operando, segundo_operando, sep="")
    #     respuesta = int(input("Respuesta: "))
    #     solucion = solucionar(primer_operando, segundo_operando, operando, respuesta)
    #     if (solucion):
    #         puntuacion = ganador(puntuacion)
    #     else:
    #         vidas = perdedor(vidas)
    #     print("\nPuntuación:", puntuacion, "\nVidas restantes:", vidas, "\n")
    # return puntuacion

# INICIO PROGRAMA

puntuacion = 0
vidas = 3
dificultad = inicializarJuego()
match dificultad:
    case 1:
        puntuacion = facil(puntuacion, vidas)
    case 2:
        puntuacion = intermedio(puntuacion, vidas)
    # case 3:
    #     puntuacion = dificil(puntuacion, vidas)
    case _:
        print("Dificultad NO válida:")
        dificultad = inicializarJuego()

print("RESULTADO FINAL:", puntuacion)
print("¡Gracias por jugar!")
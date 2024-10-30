import random

#############################################
# IN : VIDAS DISPONIBLES
# OUT: DIFICULTAD ELEGIDA
#############################################

def inicializarJuego(vidas):
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

#############################################
# IN : NONE
# OUT: INT RANDOM DEL 1 AL 10
#############################################

def random_10():
    resultado = random.randint(0,10)
    return resultado

#############################################
# IN : PUNTUACION ANTIGUAS
# OUT: PUNTUACION NUEVA
#############################################

def ganador(puntuacion):
    print("\n¡Correcto!")
    puntuacion += 1
    return puntuacion

#############################################
# IN : VIDAS ANTIGUAS
# OUT: PUNTUACION NUEVA
#############################################

def perdedor(vidas):
    print("\n¡Incorrecto!")
    vidas -= 1
    return vidas

#############################################
# IN : PRIMER OPERANDO, SEGUNDO OPERANDO, OPERANDO, RESULTADO
# OUT: BOOL CORRECTO O FALSO
#############################################

def solucionar(primer_operando, segundo_operando, operando, respuesta):
    match operando:
        case 1: # SUMA
            return primer_operando + segundo_operando == respuesta
        case 2: # RESTA
            return primer_operando - segundo_operando == respuesta
        case 3: # MULTIPLICAION
            return primer_operando * segundo_operando == respuesta
        case _: # POR SI ACASO
            return False

#############################################
# IN : PUNTUACION Y VIDAS
# OUT: PUNTUACION
#############################################

def facil(puntuacion, vidas):
    while(vidas != 0):
        primer_operando = random_10()
        segundo_operando = random_10()

        print("PREGUNTA: ", primer_operando, "x", segundo_operando, sep="")
        respuesta = int(input("Respuesta: "))

        solucion = solucionar(primer_operando, segundo_operando, 3, respuesta)

        if (solucion):
            puntuacion = ganador(puntuacion)
        else:
            vidas = perdedor(vidas)
        print("\nPuntuación:", puntuacion, "\nVidas restantes:", vidas, "\n")
    return puntuacion

#############################################
# IN : PUNTUACION Y VIDAS
# OUT: PUNTUACION
#############################################

def intermedio(puntuacion, vidas):
    while(vidas != 0):
        listaOperandos = ['+', '-', 'x']
        operando = random.randint(1,3)
        primer_operando = random_10()
        segundo_operando = random_10()

        print("PREGUNTA: ", primer_operando, listaOperandos[operando], segundo_operando, sep="")
        respuesta = int(input("Respuesta: "))

        solucion = solucionar(primer_operando, segundo_operando, operando, respuesta)
        
        if (solucion):
            puntuacion = ganador(puntuacion)
        else:
            vidas = perdedor(vidas)
        print("\nPuntuación:", puntuacion, "\nVidas restantes:", vidas, "\n")
    return puntuacion

#############################################
# IN : PUNTUACION Y VIDAS
# OUT: PUNTUACION
#############################################











#############################################
# BUCLE PRINCIPAL
#############################################

puntuacion = 0
vidas = 3
dificultad = inicializarJuego()
match dificultad:
    case 1: puntuacion = facil(puntuacion, vidas)
    case 2: puntuacion = intermedio(puntuacion, vidas)
    case _: print("Dificultad NO válida:")

print("RESULTADO FINAL:", puntuacion)
print("¡Gracias por jugar!")
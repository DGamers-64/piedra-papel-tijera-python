import random

#############################################

def inicializarJuego(vidas: int) -> str:
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

def random_10() -> int:
    resultado = random.randint(0,10)
    return resultado

#############################################

def ganador(puntuacion: int) -> int:
    print("\n¡Correcto!")
    puntuacion += 1
    return puntuacion

#############################################

def perdedor(vidas: int) -> int:
    print("\n¡Incorrecto!")
    vidas -= 1
    return vidas

#############################################

def solucionar(primer_operando: int, segundo_operando: int, operando: int, respuesta: int) -> bool:
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

def facil(puntuacion: int, vidas: int) -> int:
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

def intermedio(puntuacion: int, vidas: int) -> int:
    while(vidas != 0):
        lista_operandos = ['+', '-', 'x']
        operando = random.randint(1,3)
        primer_operando = random_10()
        segundo_operando = random_10()

        print("PREGUNTA: ", primer_operando, lista_operandos[operando-1], segundo_operando, sep="")
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

def dificil(puntuacion: int, vidas: int) -> int:
    while(vidas != 0):
        lista_operandos = ['+', '-', 'x']
        operando = random.randint(1,3)
        primer_operando = random_10()
        segundo_operando = random_10()
        
        match operando:
            case 1:
                resultado = primer_operando + segundo_operando
            case 2:
                resultado = primer_operando - segundo_operando
            case 3:
                resultado = primer_operando * segundo_operando

        lista_simbolos_a_quitar = [primer_operando, segundo_operando, resultado]
        simbolo_quitar = random.randint(0, len(lista_simbolos_a_quitar))

        match simbolo_quitar:
            case 1:
                print("PREGUNTA: ", "?", lista_operandos[operando-1], segundo_operando, "=", resultado, sep="")
                respuesta = int(input("Respuesta: "))
                if(respuesta == primer_operando):
                    puntuacion = ganador(puntuacion)
                else:
                    vidas = perdedor(vidas)
            case 2:
                print("PREGUNTA: ", primer_operando, lista_operandos[operando-1], "?", "=", resultado, sep="")
                respuesta = int(input("Respuesta: "))
                if(respuesta == segundo_operando):
                    puntuacion = ganador(puntuacion)
                else:
                    vidas = perdedor(vidas)
            case 3:
                print("PREGUNTA: ", primer_operando, lista_operandos[operando-1], segundo_operando, "=", "?", sep="")
                respuesta = int(input("Respuesta: "))
                if(respuesta == resultado):
                    puntuacion = ganador(puntuacion)
                else:
                    vidas = perdedor(vidas)
        
        print("\nPuntuación:", puntuacion, "\nVidas restantes:", vidas, "\n")
    return puntuacion

#############################################
# BUCLE PRINCIPAL
#############################################

puntuacion = 0
vidas = 3
dificultad = inicializarJuego(vidas)
match dificultad:
    case 1: puntuacion = facil(puntuacion, vidas)
    case 2: puntuacion = intermedio(puntuacion, vidas)
    case 3: puntuacion = dificil(puntuacion, vidas)
    case _: print("Dificultad NO válida:")

print("RESULTADO FINAL:", puntuacion)
print("¡Gracias por jugar!")
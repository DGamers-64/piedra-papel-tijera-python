

def dificil(puntuacion, vidas):
    listaSimbolos = [primer_operando, segundo_operando, resultado]
    simbolo_quitar = random.randint(listaSimbolos)
    while(vidas != 0):
        listaOperandos = ['+', '-', 'x']
        operando = random.randint(1,3)
        primer_operando, segundo_operando = preguntar_aleatorio()
        print("PREGUNTA: ", primer_operando, listaOperandos[operando], segundo_operando, sep="")
        respuesta = int(input("Respuesta: "))
        solucion = solucionar(primer_operando, segundo_operando, operando, respuesta)
        if (solucion):
            puntuacion = ganador(puntuacion)
        else:
            vidas = perdedor(vidas)
        print("\nPuntuación:", puntuacion, "\nVidas restantes:", vidas, "\n")
    return puntuacion

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

print("RESULTADO FINAL:", puntuacion)
print("¡Gracias por jugar!")
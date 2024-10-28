import random

def preguntar_aleatorio():
    primer_operando = random.randint(0,10)
    segundo_operando = random.randint(0,10)
    print("PREGUNTA: ", primer_operando, "x", segundo_operando, sep="")
    respuesta = int(input("Respuesta: "))
    return primer_operando, segundo_operando, respuesta

def solucionar(primer_operando, segundo_operando, resultado):
    if (primer_operando * segundo_operando == resultado):
        return "CORRECTO!!!"
    return "INCORRECTO!!!"

p, s, r = preguntar_aleatorio()
print(solucionar(p, s, r))

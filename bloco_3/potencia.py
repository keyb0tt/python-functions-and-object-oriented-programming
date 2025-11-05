# Exercício 11: Crie potencia(base, expoente=2) onde o expoente padrão é 2.
import os
os.system('clear')

def potencia(base, expoente=2):
    result = base

    for i in range(1, expoente):
        result *= base

    return result

potencia_um = potencia(15)
potencia_dois = potencia(4, 3)
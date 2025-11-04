# Exercício 8: Desenvolva inverter_string(texto) que retorna a string invertida.
import os
os.system('clear')

def inverter_string(texto):
    texto = list(texto)
    texto_temp = list('')

    for i in range(len(texto), 0, -1):
        texto_temp.append(texto[i - 1])

    return ''.join(texto_temp)

print(inverter_string('cachorro'))
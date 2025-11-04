# Exercício 7: Faça contar_vogais(texto) que conta quantas vogais existem em uma string.
import os
os.system('clear')

def contar_vogais(texto):
    vogais = 'aeiouAEIOU'
    vogais_count = 0
    
    caracteres = list(texto)

    for caracter in caracteres:
        if caracter in vogais:
            vogais_count += 1

    return vogais_count

print(contar_vogais('cachorro'))
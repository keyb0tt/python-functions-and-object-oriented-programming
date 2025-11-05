# Exercício 10: Faça eh_palindromo(palavra) que verifica se uma palavra é palíndromo (ex: "arara").
import os
os.system('clear')

def eh_palindromo(palavra):
    lista_letras_original = list(palavra)
    lista_letras_reversed = []

    for i in range(len(lista_letras_original), 0, -1):
        lista_letras_reversed.append(lista_letras_original[i - 1]) 

    palavra = ''.join(lista_letras_original)
    palavra_reversed = ''.join(lista_letras_reversed)

    if palavra.lower() == palavra_reversed.lower():
        return True
    else:
        return False

print(eh_palindromo('arara'))
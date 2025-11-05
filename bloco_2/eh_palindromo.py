# Exercício 10: Faça eh_palindromo(palavra) que verifica se uma palavra é palíndromo (ex: "arara").
import os
os.system('clear')

def eh_palindromo(palavra):
    lista_palavra = list(palavra)
    letras_reversed = []
    print(lista_palavra)

    for i in range(len(lista_palavra) - 1, 0, -1):
        print(lista_palavra[i])
        letras_reversed.append(lista_palavra[i]) 

    print(letras_reversed)
    pass

print(eh_palindromo('cachorro'))
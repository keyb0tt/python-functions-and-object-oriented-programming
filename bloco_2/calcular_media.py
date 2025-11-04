# Exercício 6: Crie calcular_media(nota1, nota2, nota3) que retorna a média aritmética de três notas.
import os
os.system('clear')

def calcular_media(nota1, nota2, nota3):
    soma_notas = nota1 + nota2 + nota3

    return round(soma_notas / 3, 1)

print(calcular_media(10, 5, 5))
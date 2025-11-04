# Exercício 5: Desenvolva maior_de_dois(a, b) que retorna o maior entre dois números.
import os
os.system('clear')

def maior_de_dois(a, b):
    maior = a

    if b > a:
        maior = b
    return maior

print(maior_de_dois(5, 10))
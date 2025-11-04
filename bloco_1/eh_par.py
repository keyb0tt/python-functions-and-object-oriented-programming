# Exercício 3: Faça uma função eh_par(numero) que retorna True se o número for par e False caso contrário.
import os
os.system('clear')

def eh_par(numero):
    if numero % 2 == 0:
        return True
    else:
        return False
    
print(eh_par(12))
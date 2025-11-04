# Exercício 9: Crie calcular_imc(peso, altura) que calcula o Índice de Massa Corporal (IMC = peso / altura²).
import os
os.system('clear')

def calcular_imc(peso, altura):
    return peso / (altura * altura)

print(calcular_imc(88, 1.70))
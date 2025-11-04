# Exercício 4: Crie temperatura_fahrenheit(celsius) que converte temperatura de Celsius para Fahrenheit (F = C × 1.8 + 32).
import os
os.system('clear')

def temperatura_fahrenheit(celsius):
    tempF = celsius * 1.8 + 32

    return round(tempF)

print(temperatura_fahrenheit(40))
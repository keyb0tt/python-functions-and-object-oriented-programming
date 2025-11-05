# Exercício 14: Crie repetir_texto(texto, vezes=3) que repete um texto N vezes.
def repetir_texto(texto, vezes=3):
    for i in range(vezes):
        print(texto)

    pass

texto = 'Cachorro quente 5 real'
print(repetir_texto(texto))
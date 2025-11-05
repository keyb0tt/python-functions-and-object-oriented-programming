# Exercício 15: Desenvolva formatar_moeda(valor, simbolo="R$") que formata um número como moeda.
def formatar_moeda(valor, simbolo='R$'):

    string_formatada = f'{simbolo}{round(valor, 2):.2f}'

    return string_formatada

valor_formatado = formatar_moeda(120.50)
print(valor_formatado)


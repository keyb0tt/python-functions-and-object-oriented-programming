# Exercício 13: Faça desconto(valor, percentual=10) que aplica um desconto (padrão 10%) ao valor.
def desconto(valor, percentual=10):
    desconto_compra = valor * 0.1
    valor_final = valor - desconto_compra

    return valor_final

compra_descontada = round(desconto(1200), 2)

print(compra_descontada)
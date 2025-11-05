# Exercício 12: Desenvolva criar_email(nome, dominio="gmail.com") que cria um email no formato nome@dominio.
def criar_email(name, domain='gmail.com'):
    invalid_char_name = ['<', '>', ',', ':', ';', '&', '+', '=', ' ']

    for caracter in name:
        if caracter in invalid_char_name:
            return False
        
    if '.' not in domain:
        return False
    
    result_email = name + '@' + domain

    return result_email

usuario1_email = criar_email('kaiqueboscoaraujo')
usuario2_email = criar_email('cachorro', 'hotmail.com')
usuario3_email = criar_email('ca:chorro')
usuario4_email = criar_email('hotdog', 'hotmailcom')

print(usuario1_email)
print(usuario2_email)
print(usuario3_email)
print(usuario4_email)
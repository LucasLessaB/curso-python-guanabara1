print('====== DESAFIO 20 ======')
print('=== Analisador de Nomes =====')
def analisador_nome(nome):
    print('Seu nome com letras maiusculas:{}'.format(nome.upper()))
    print('Seu nome com letras minusculas:{}'.format(nome.lower()))
    print('Seu nome tem {} letras'.format(len(nome) - nome.count(' ')))
    print('Seu primeiro nome tem {} letras'.format(nome.find(' ')))

nome = input('Digite seu nome:')
analisador_nome(nome)
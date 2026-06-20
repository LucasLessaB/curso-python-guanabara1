import datetime
print('====== DESAFIO 039 ======')
ano_nascimento = int(input('Digite o ano do seu nasciemento:'))
maioridade =datetime.date.today().year - ano_nascimento
if maioridade > 18 :
    print('VocÊ tem que se alistar IMEDIATAMENTE')
    print('JÁ PASSOU FOI {} anos'.format(maioridade - 18))
    print('Você deveria ter se alistado em {}'.format(ano_nascimento + 18))
elif maioridade < 18:
    print('Você tem {} anos, não precisa se alistar agora'.format(maioridade))
    print('você vai se alistar em {} anos'.format( 18 - maioridade))
    print('No ano de {}'.format(ano_nascimento + 18))
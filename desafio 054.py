import datetime
maioridade = 0
menoridade = 0
for c in range(1,7):
    anoN = int(input('Digite a data de nascimento {}:'.format(c)))
    if datetime.date.today().year - anoN >= 18:
        maioridade += 1
    else:
        menoridade += 1
print('''Foram contabilizados {} pessoas.
Sendo {} deles maiores de 18 anos.
E {} deles são menores de 18 anos.'''.format(maioridade + menoridade, maioridade, menoridade))


print('===== DESAFIO 034 =====')
salario = float(input('Qual o seu salario: '))
if salario > 1250:
    salario = salario + (salario * 0.10)
    print('Seu salario passa a ser R${:.2f}'.format(salario))
else:
    salario = salario + (salario * 0.15)
    print('Seu salario passara a ser R${:.2f}'.format(salario))
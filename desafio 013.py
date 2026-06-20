print('====== DESAFIO 013 ======')
salario = float(input('Informe o salario atual:'))
reajuste = (salario * 0.15) + salario
print('O salario era de R${:.2f}'.format(salario))
print('Com o resjuste ficará R${:.2f}'.format(reajuste))
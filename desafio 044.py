print('===== DESAFIO 044 =====')
valor = float(input('Qual o valor da copra? R$ '))
print('''Escolha uma forma de pagamento:
[1] Dinheiro/cheque/pix
[2] A vista no cartão.
[3] 2x no cartão 
[4] 3x ou mais no cartão.''')
escolha = str(input('Escolha uma opção:'))
if escolha == '4':
   quantidadep = int(input('Deseja pagarem quantas parcelas?'))
   print('A compra foi dividida em {} vezes'.format(quantidadep))
   print('Cada parcela saiu por R${:.2f}'.format((valor + (valor * 0.20))/ quantidadep))
   print('TOTAL : R${:.2f}'.format((valor + (valor * 0.20))))
elif escolha == '3':
    print('A compra foi dividida em 2x de R${}'.format(valor/2))
elif escolha == '2':
    print('Você obteve um descontp 10% o valor fica R${:.2f}'.format(valor - (valor * 0.10)))
elif escolha == '1':
    print('Você obteve um desconto de 20% o valor da fica R${:.2f}'.format(valor - (valor * 0.20)))

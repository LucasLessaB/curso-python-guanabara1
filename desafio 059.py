print('===== DESAFIO 059 =====')
sair =  False
while not sair:
 n1 = int(input('Primeiro valor: '))
 n2 = int(input('Segundo valor: '))
 while not sair:
  print('''ESCOLHA UMA DAS OPÇÕES ABAIXO:
[1] Somar
[2] Multiplicar
[3] Maior
[4] Novos números
[5] SAIR DO PROGRAMA''')
  escolha = int(input('Escolha a opção:'))
  if escolha == 1:
   soma = n1 + n2
   print('A soma de: {} + {} = {}'.format(n1, n2, soma))
  elif escolha == 2:
   multiplicar = n1 * n2
   print('A multiplicação de: {} * {} = {}'.format(n1, n2, multiplicar))
  elif escolha == 3:
   print('O maior número é:',max(n1, n2))
  elif escolha == 4:
    break
  elif escolha == 5:
      print('Finalizando...')
      sair = True




while True:
  num = int(input('Digite um numero para ver sua tabuada: '))
  if num < 0:
    print('Programa finalizado com sucesso. Volte sempre!')
    break
  else:
    for c in range(1,11,1):
      print(f'{num} x {c} = {num*c}')

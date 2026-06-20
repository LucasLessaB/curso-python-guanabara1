print('====== DESAFIO 050 ======')
contador = 0
pares = 0
for c in range(1,7):
    num = int(input('Digite o valor {}: '.format(c)))
    if num % 2 == 0:
     pares += num
     contador += 1
print(f'A quantidade de pares digitadas foi {contador}.')
print(f'A soma de pares digitados foi {pares}.')
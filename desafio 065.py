nums = []
parada = False
while not parada:
    num = int(input('Digite um numero:'))
    nums.append(num)
    continuer = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    if continuer == 'N':
     parada = True
     print('''Você digito {} numeros , a media é {}.
O maior número é {} , o menor número {}.
'''.format(len(nums),(sum(nums)/len(nums)),max(nums),min(nums)))
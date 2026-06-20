print('===== DESAFIO 009 =====')
num = int(input('Digite um numero para ver a sua tabuada:'))
for c in range(1,11,1):
    print('{} x {:2} = {}'.format(num,c,num*c))
print('===== DESAFIO 006 =====')
def analisar(num):
    print('O dobro de {} é {}'.format(num, num*2))
    print('O triplo de {} é {}'.format(num, num*3))
    print('A raíz quadrada de {} é {}'.format(num, num**(1/2)))

num = int(input('Digite um numero:'))
analisar(num)

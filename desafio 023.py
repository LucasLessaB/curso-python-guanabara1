print('====== DESAFIO 023 ======')
print('===== Separador de números =====')
def analisar(num):
    u = num // 1 % 10
    d = num // 10 % 10
    c = num // 100 % 10
    m = num // 1000 % 10
    print('Analizando o número {}'.format(num))
    print('Unidade:{}'.format(u))
    print('Dezena:{}'.format(d))
    print('Centena:{}'.format(c))
    print('Milhar:{}'.format(m))

num = int(input('Digite um número:'))
analisar(num)
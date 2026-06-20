soma = []
while True:
    num = int(input('Digite um numero [999 para parar]: '))
    if num != 999:
        soma.append(num)
    else:
        print(f'Foram digitados {len(soma)} números, e a soma é {sum(soma)}')
        break
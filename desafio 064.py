soma = []
parada = False
while not parada:
    num = int(input('Digite um numero [999 para parar]: '))
    if num == 999:
        print('Foram digitados {} numeros, e a soma é {}'.format(len(soma),sum(soma)))
        parada = True
    elif num != 999:
        soma.append(num)
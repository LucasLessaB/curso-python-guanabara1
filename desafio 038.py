print('=====DESAFIO 038=====')
numeros = []
for n in range(1,3):
    num = int(input('digite um numero: '))
    numeros.append(num)
if numeros[0] > numeros[1]:
    print('O primeiro numero é o maior')
elif numeros[0] < numeros[1]:
    print('O segundo numero é o maior')
else:
    print('Os numeros são iguais')
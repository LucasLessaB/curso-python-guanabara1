print('Gerador de Fibonacci')
n = int(input('Quantos termos deseja mostrar? '))

a = 0
b = 1
contador = 0

while contador < n:
    print(a, end='_')
    novo = a + b
    a = b
    b = novo
    contador += 1
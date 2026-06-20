import random
print('==== DESAFIO 058 ====')
print('==== JOGO DE ADIVINHAÇÃO')
valor = random.randint(1, 10)
print('-=-' * 20)
print('Eu pensei em um número entre 1 e 10')
acertou = False
while not acertou:
    print('Você consegue adivinhar?')
    resposta = int(input('Digite um valor entre 1 e 10: '))
    if resposta != valor:
        print('Parabens você acertou')
        if resposta > valor:
         print('Você pensei em menos')
        elif resposta < valor:
         print('Eu pensei em mais')
    else:
         print('Parabens você acertou')
         acertou = True


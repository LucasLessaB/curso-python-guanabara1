import random
print('Vamos jogar Par ou Impar')
#contador de vitorias:
win = 0
#sistema do jogo:
while True:
    pc = random.randint(1, 10)
    entrada = str(input('Par ou Impar [P/I]')).strip().upper()
    valor = int(input('Digite um valor: '))
    if entrada == 'P' and (valor + pc) % 2 == 0:
           print('Você escolheu Par e ganhou')
           print(f'Você colocou{valor} e o computador escolheu {pc}')
           win += 1
    elif entrada == 'P' and (valor + pc) % 2 != 0:
           print('Você escolheu Par e perdeu')
           print(f'Você colocou {valor} e o computador escolheu {pc}')
           print(f'Você teve {win} vitorias consecutivas ')
           break
    elif entrada == 'I' and (valor + pc) % 2 == 1:
           print('Você escolheu Impar e ganhou')
           print(f'Você colocou {valor} e o computador escolheu {pc}')
           win += 1
    elif entrada == 'I' and (valor + pc) % 2 != 1:
           print('Você escolheu Impar e perdeu')
           print(f'Você colocou {valor} e o computador escolheu {pc}')
           print(f'Voce teve {win} vitorias consecutivas ')
           break

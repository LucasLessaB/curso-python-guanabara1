import random
print('{:=^40}'.format(' DESAFIO 045 '))
print('==== PEDRA, PAPEL , TESOURA ====')
valor = random.randint(1, 3)
print('''ESCOLHA UMA OPÇÃO:
[ 1 ] PEDRA
[ 2 ] PAPEL
[ 3 ] TESOURA''')
escolha = int(input('Digite a opção: '))
if escolha == 1:
    if valor == 1:
        print('EMPATE')
    elif valor == 2:
        print('DERROTA')
    else:
        print('VITORIA')
elif escolha ==2 :
    if valor == 1:
        print('VITORIA')
    elif valor == 2:
        print('EMPATE')
    else:
        print('DERROTA')
elif escolha == 3:
    if valor == 1:
        print('DERROTA')
    elif valor == 2:
        print('VITORIA')
    else:
        print('EMPATE')
else:
    print('Opção invalida')
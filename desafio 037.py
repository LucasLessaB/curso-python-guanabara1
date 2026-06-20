print('====== DESAFIO 037 ======')
num = int(input('Digite um numero:'))
print('''ESCOLHA UMA DAS OPÇÕES ABAIXO
[1]===== BINARIO ======
[2]===== HEXADECIMAL =====
[3]===== OCTAL ======''')
escolha = int(input('Qual a sua escolha:'))
if escolha == 1:
    print('O valor binatio é {}.'.format(bin(num)))
elif escolha == 2:
    print('O valor hexadecimal é {}.'.format(hex(num)))
elif escolha == 3:
    print('O valor octal é {}.'.format(oct(num)))
else:
    print('Opção invalida')
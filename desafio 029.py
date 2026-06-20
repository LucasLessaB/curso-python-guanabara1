import random
import time
('=====DESAFIO 029=====')
num = random.randint(1,10)
time.sleep(2)
print('Vou pensar em um numero entre 1 e 10')
time.sleep(2)
print('tente adivinhar o numero que eu pensei')
time.sleep(2)
valor = int(input('Digite um número de 1 a 10: '))
if valor != num:
    print('hahaha você errou...')
elif valor == num:
    print('Você acertou')

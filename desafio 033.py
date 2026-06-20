print('===== DESAFIO 033 =====')
nums = []
for c in range(1,4):
    numero = int(input('Diga um numero: '))
    nums.append(numero)
print(' O maior numero é {}'.format(max(nums)))
print(' O menor numero é {}'.format(min(nums)))
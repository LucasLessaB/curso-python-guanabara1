import random
print('==== DESAFIO 20 ====')
print('===== SORTEADOR DE NOMES =====')
nomes = []
for c in range(0,5):
    nomes.append(str(input('Digite um nome:')))
random.shuffle(nomes)
print(nomes)
import random
nomes = []
print('==== DESAFIO 019 ====')
for i in range (1,6):
    nome=input('Digite um nome:')
    nomes.append(nome)
print(random.choice(nomes))
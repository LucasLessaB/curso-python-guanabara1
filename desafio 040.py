print('====== DESAFIO 040 ======')
print('Avaliador de notas')
notas = []
for n in range(1,3):
    notas.append(float(input('Digite a nota:')))
media = sum(notas)/2
if media >= 7:
    print('Tirando {} e {} a media é {:.2f}'.format(notas[0],notas[1],media))
    print('Aluno aprovado')
elif media >= 5:
    print('Tirando {} e {} a media é {:.2f}'.format(notas[0],notas[1],media))
    print('Aluno e recuperação')
else:
    print('Tirando {} e {} a media é {:.2f}'.format(notas[0],notas[1],media))
    print('Aluno reprovado')
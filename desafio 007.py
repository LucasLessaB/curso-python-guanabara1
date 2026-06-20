print('====== DESAFIO 007 ======')
nome_aluno = input('Digite o nome do aluno: ').capitalize()
nota1 = float(input('Digite a primeira nota:'))
nota2 = float(input('Digite a segunda nota:'))
media = (nota1 + nota2)/2
print('O aluno(a): {} teve a média das notas {:.2f}'.format(nome_aluno, media))
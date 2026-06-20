maioridade_homem = 0
nomevelho = ""
idade_media = []
mulher20 = 0
for c in range(1,5):
    nome = str(input('Digite o nome da {}º pessoa: '.format(c)))
    idade = int(input('Digite a idade da {}º pessoa:'.format(c)))
    idade_media.append(idade)
    sexo = str(input('Digite o sexo da {}º pessoa: '.format(c))).upper()
    if c == 1 and sexo == 'M':
        maioridade_homem = idade
        nomevelho = nome
    if sexo == 'M' and idade > maioridade_homem:
        maioridade_homem = idade
        nomevelho = nome
    if sexo == 'F' and idade < 20:
        mulher20 += 1
media = sum(idade_media) / len(idade_media)
print('A idade do homem mais velho é {} anos, e seu nome é {}'.format(maioridade_homem, nomevelho))
print('São ao todo {} mulheres com menos de 20 anos'.format(mulher20))
print('E a media do grupo é {}'.format(media))
c_maioridade = 0
c_homens = 0
c_mulheres20 = 0
parada = False
while not parada:
    idade = int(input('Informe a idade:'))
    sexo = str(input('Informe o sexo:[M/F]')).upper()
    if idade > 18:
        c_maioridade += 1
    if sexo == 'M':
        c_homens += 1
    if sexo == 'F' and idade < 20:
        c_mulheres20 += 1
    continuar = str(input('Quer continuar?[S/N]')).upper()
    if continuar == 'N':
        break
print(f'Foram cadastrados {c_homens}  homems no programa')
print(f'Foram cadastradas {c_mulheres20} mulheres com menos de 20 anos')
print(f'Foram cadastras {c_maioridade} pessoas com mais de 18 anos')
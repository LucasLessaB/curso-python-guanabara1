contador = 0
num = int(input('digite um numero inteiro: '))
for c in range(1,num+1):
    if num % c == 0:
      print(c, end=' ')
      contador += 1
if contador > 2:
    print('O número não é primo,ele foi dividido por todos esse numeros.')
else:
    print('O número é primo, ele foi dividido apenas por 1 e ele mesmo')



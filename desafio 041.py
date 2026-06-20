import datetime
print('====== DESAFIO 041 ======')
anoN= int(input('Digite o anao de nasciento do atleta:'))
idade = anoN - datetime.date.today().year
if idade > 9 :
    print('Atleta categoria : MIRIM')
elif idade > 14:
    print('Atleta categoria : INFANTIL')
elif idade > 19 :
    print('Atleta categoria : JUNIOR')
elif idade > 25 :
    print('Atleta categoria : SENIOR')
else :
    print('Atleta categoria : MASTER')

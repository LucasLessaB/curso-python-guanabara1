print('===== DESAFIO 043 =====')
kg = float(input('Qual o seu peso em KG:'))
alt = float(input('Qual a sua altura em Metros:'))
imc = kg / alt**2
if imc < 18.5:
    print('Abaixo do peso')
elif imc >= 18.5 and imc <= 25:
    print('Peso ideal')
elif imc >= 25 and   imc <= 30:
    print('Sobrepeso')
elif imc >= 30 and imc <= 40:
    print('Obesidade')
else:
    print('Obesidade Morbida')
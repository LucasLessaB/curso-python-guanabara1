print('===== DESAFIO 042 =====')
a = int(input('Informe o primeiro segmento: '))
b = int(input('Informe o segundo segmento: '))
c = int(input('Informe o terceiro segmento: '))

if a < b + c and b < a + c and c < a + b:
    if a == b == c:
        print('TRIANGULO EQUILOROUS')
    elif a == b !=c or a == c != b or b == c != a:
        print('TRIANGULO ISOSCELES')
    elif a != b != c != a != b != c:
        print('TRIANGULO ESCALENO')
else:
    print('Não é um triangulo.')






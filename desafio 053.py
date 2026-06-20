frase = str(input('Digite uma frase: ')).strip().upper()
frase = frase.replace(' ','0')
frase1 = reverso = frase[::-1]
print('A FRASE DE TRAS PARA FRENTE É: {}'.format(frase1))
if frase1 == frase:
    print('A frase é um palindromo')
else:
    print('A frase não é um palindromo')
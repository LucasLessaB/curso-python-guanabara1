print('===== DESAFIO 028 =====')
velocidade = int(input('Qual a velocidade atual do carro:'))
if velocidade <=80:
    print('Ta safe meu patrão pode ir...')
elif velocidade >= 80:
    print('TA DOIDÃO , PEGA PRA FICAR ESPERTO...')
    print('Multa de R${:.2f}'.format((velocidade - 80) * 7))
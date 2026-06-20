print('=====DESAFIO 031=====')
distancia = int(input('Qual a distancia da viagem: '))
if distancia <= 200:
    print('A viagem vai custar R${:.2f}'.format(distancia * 0.5))
elif distancia > 200:
    print('A viagem vai custar R${:.2f}'.format(distancia * 0.45))

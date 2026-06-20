print('===== DESAFIO 011 =====')
altura = float(input('Informe a altura da parede em metros:'))
largura = float(input('Informe a largura da parede em metros:'))
m2 = largura * altura
tinta = m2 / 2
print('Sua parede tem {:.2f} metros quadrados'.format(m2))
print('E vai precisar {:.2f} litros de tinta'.format(tinta))
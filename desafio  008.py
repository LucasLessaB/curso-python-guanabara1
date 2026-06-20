print('====== DESAFIO 8 ======')
medida = float(input('Digite a medida em metros: '))
cm = medida * 100
mm = medida * 1000
km = medida / 1000
print('A medida de {}M é igual a {:.2f}CM e {:.2f}MM'.format(medida,cm,mm))
print('A medida de {}M é igual a {}KM.'.format(medida,km))
print('====== DESAFIO 004 ======')
def analisar(algo):
 print('O tipo primitivo é {}'.format(type(algo)))
 print('É numerico?',algo.isnumeric())
 print('É alfabetico?',algo.isalpha())
 print('É alphanumerico?',algo.isalnum())
 print('Está em maiuscula?',algo.isupper())
 print('Está em minuscula?',algo.islower())

algo = input('Digite algo: ')
print(analisar(algo))
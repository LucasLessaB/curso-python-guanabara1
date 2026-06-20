print('====== DESAFIO 018 ======')
print('==== SENO, COSSENO, TANGENTE ====')
print('====== TRIANGULO RETANGULO  ======')
cateto_adjacente = float(input('Digite o valor do cateto adjacente:'))
cateto_oposto = float(input('Digite o valor do cateto oposto:'))
hipotenusa =(( cateto_oposto ** 2) + (cateto_adjacente ** 2)) ** (1/2)
seno = cateto_oposto / hipotenusa
cosseno = cateto_adjacente / hipotenusa
tangente = cateto_oposto / cateto_adjacente
print('A hipotenusa é {:.2f}'.format(hipotenusa))
print('O seno é {:.2f} , o cosseno é {:.2f}  e o tangete é {:.2f}'.format(seno, cosseno, tangente))

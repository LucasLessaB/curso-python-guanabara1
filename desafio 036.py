print('===== DESAFIO 036 =====')
valor_da_casa = int(input('Informe o valor da casa:'))
salario = float(input('Informe o seu salario:'))
anos_pagamento = int(input('Informe quantos anos deseja pagar: '))
parcela = ( valor_da_casa / 12 ) / anos_pagamento
salario_seguro = salario - (salario * 0.70)
if parcela < salario_seguro:
    print('Emprestimo aprovado')
else :
    print('Emprestimo negado')
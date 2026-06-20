pessoas = []
for k in range (1,6):
    kg = float(input('Digite o peso de  {}º pessoa em kg: '.format(k)))
    pessoas.append(kg)
print(max(pessoas),'kg')
print(min(pessoas),'kg')
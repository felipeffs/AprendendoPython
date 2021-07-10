a = str(input('Nome Completo: ')).strip()

ab = a.split()

print('Nome todo em minúsculo: {}'.format(a.lower()))
print('Nome todo em maiúsculo {}'.format(a.upper()))
print('Quantidade de letras sem contar espaços: {}'.format(len(a) - a.count(' ')))
print('Quantidade de letras no primeiro nome: {}'.format(len(ab[0])))

# ex: João Alberto de Oliveira Ramos

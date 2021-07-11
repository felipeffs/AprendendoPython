"""
Escreva um programa para aprovar o empréstimo bancário para a
compra de uma casa. Pergunte o valor da casa, o salário do comprador
e em quantos anos ele vai pagar.
A prestação mensal, não pode exceder 30% do salário ou então o
empréstimo será negado.
"""

print('Banco Vita >> Financiamento de Imóveis\n')

valorCasa = float(input('\tValor da Casa: \033[32mR$\033[m'))
salario = float(input('\tSua renda mensal: \033[32mR$\033[m'))
parcelamento = int(input('\tEm quantos anos pretende pagar: '))

prestacao = valorCasa / (parcelamento * 12)

if prestacao > (salario * 0.3):
    print('\t\033[31mVocê não pode financiar esta casa\033[m')
else:
    print('\t\033[36mO valor da prestação é de {:.2f}\033[m'.format(prestacao))

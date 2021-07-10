print('Banco Vita >> Financiamento de Imóveis\n')

valorcasa = float(input('\tValor da Casa: \033[32mR$\033[m'))
salario = float(input('\tSua renda mensal: \033[32mR$\033[m'))
parcelamento = int(input('\tEm quantos anos pretende pagar: '))

prestacao = valorcasa / (parcelamento * 12)

if prestacao > (salario * 0.3):
    print('\t\033[31mVocê não pode financiar esta casa\033[m')
else:
    print('\t\033[36mO valor da prestação é de {:.2f}\033[m'.format(prestacao))

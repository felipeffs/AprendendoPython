quantMulher = 0
idadeG = 0
velhoN = ''
velhoI = 0
for c in range(0, 4):
    print('=='*21)
    nome = str(input('Nome da Pessoa: '))
    idade = int(input('Idade: '))
    sexo = str(input('Sexo: ')).strip()
    print('==' * 21)
    if sexo.upper() == 'M':
        if c == 0:
            velhoN = nome
            velhoI = idade
        elif idade > velhoI:
            velhoN = nome
            velhoI = idade
    if (sexo.upper() == 'F') & (idade < 20):
        quantMulher += 1
    idadeG += + idade
idadeG = idadeG / 4
print('A média de idade do grupo é de {} anos'.format(idadeG))
if velhoN != '':
    print('O homem mais velho tem {} anos e se chama {} '.format(velhoI, velhoN))
print('E tem {} mulher(es) com menos de 20 anos'.format(quantMulher))

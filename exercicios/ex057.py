nome = str(input('Digite o Nome Completo: ')).strip().title()
s = str(input('Sexo [M/F]: ')).strip().upper()[0]
while s not in 'MF':
    print('Dado Inválido! Informe novamente.')
    s = str(input('Sexo [M ou F]: ')).strip().upper()[0]

print('Nome: {}\n'
      'Sexo: {}'.format(nome, s))

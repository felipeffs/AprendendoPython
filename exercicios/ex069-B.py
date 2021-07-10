maior = mMulheres = tHomens = 0
while True:
    print('='*40)
    idade = int(input('Idade: '))
    sexo = ' '
    while sexo not in 'FM':
        sexo = str(input('Sexo: [M/F] ')).upper().strip()[0]
    if idade > 18:
        maior += 1
    if sexo == 'F' and idade < 20:
        mMulheres += 1
    elif sexo == 'M':
        tHomens += 1
    print('='*40)
    cond = ' '
    while cond not in 'SN':
        cond = str(input('Deseja Continuar? [S/N] ')).upper().strip()[0]
    if cond == 'N':
        break
print('=' * 40)
print(f'\n>>Informações:\n'
      f'-Pessoas com mais de 18 anos: {maior}\n'
      f'-Homens cadastrados: {tHomens}\n'
      f'-Mulheres com menos de 18 anos: {mMulheres}')

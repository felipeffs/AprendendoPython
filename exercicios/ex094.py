pessoas = list()
while True:
    while True:
        quant = str(input('Quantas pessoas deseja cadastrar? ')).strip()
        if quant.isdigit():
            quant = int(quant)
            break
    if quant == 0:
        break
    for q in range(0, quant):
        print('='*50)
        while True:
            nome = str(input('Nome: ')).strip().title()
            n = nome.replace(' ', '')
            if n.isalpha():
                break
            print('\033[31mNome Inválido! Digite novamente.\033[m')
        print('-' * 50)
        while True:
            sexo = str(input('Sexo: [M/F] ')).strip()[0].upper()
            if sexo in 'MF':
                break
            print('\033[31mSexo Inválido! Digite novamente.\033[m')
        print('-' * 50)
        while True:
            idade = str(input('Idade: ')).strip()
            if idade.isdigit():
                idade = int(idade)
                if idade > 0:
                    break
            print('\033[31mIdade Inválida! Digite novamente.\033[m')
        print('=' * 50)
        pessoas.append({'nome': nome, 'sexo': sexo, 'idade': idade})
total = len(pessoas)
print('=' * 50)
print(f' — Quantidade de pessoas no grupo: {total}')
media = 0
for p in pessoas:
    media += p['idade']
if total > 0:
    media = media/total
    print(f' — A média de idade é de {media:.2f}')
    print(f' — As mulheres cadastradas: ', end='')
    for p in pessoas:
        if p['sexo'] == 'F':
            print(f'-> {p["nome"]}', end=' ')
    print()
    if total > 1:
        print('—' * 50)
        print(f'{"Lista de pessoas acima da média de idade":^50}')
        for p in pessoas:
            if p['idade'] > media:
                print('—'*50)
                print(f'\t Nome: {p["nome"]}\n'
                      f'\t Sexo: {p["sexo"]}\n'
                      f'\t Idade: {p["idade"]}')
        print('—'*50)

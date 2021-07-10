pessoas = list()
dados = list()
resp = 0
while True:
    for c in range(0, resp):
        print('='*50)
        # Só strings
        while True:
            dados.append(str(input('Nome da Pessoa: ')).strip().title())
            d = dados[0].replace(' ', '')
            if d.isalpha():
                break
            dados.clear()
            print('\033[31mNome inválido! Digite novamente\033[m')
        # Só números
        while True:
            d1 = str(input('Peso: ')).strip()
            d2 = d1.replace('.', '')
            if d2.isdigit():
                dados.append(float(d1))
                break
            print('\033[31mPeso inválido! Digite novamente\033[m')
        # Copiar dados (COPIAR -> [:]) para a lista pessoas e apagar os dados
        pessoas.append(dados[:])
        dados.clear()
    print('=' * 50)
    # Quer Continuar?
    while True:
        resp = str(input("Quantas pessoas quer cadastrar? "))
        if resp.isdigit():
            resp = int(resp)
            break
        print('\033[31mQuantidade Inválida, digite novamente.\033[m')
    if resp == 0:
        break
print('='*50)
print(f'Pessoas Cadastradas: {len(pessoas)}')
maior = menor = 0
for pos, p in enumerate(pessoas):
    if pos == 0:
        maior = p[1]
        menor = p[1]
    elif maior < p[1]:
        maior = p[1]
    elif menor > p[1]:
        menor = p[1]

print(f'O maior peso foi {maior}Kg. Peso de ', end='')

maiorNomes = list()
for p in pessoas:
    if p[1] == maior:
        maiorNomes.append(p[0])

tam = len(maiorNomes)
for pos, m in enumerate(maiorNomes):
    if tam == 1 or pos == tam - 1:
        print(f'{m}.')
    elif pos < tam - 2:
        print(f'{m}, ', end='')
    elif pos == tam - 2:
        print(f'{m} e ', end='')

print(f'O menor peso foi {menor}Kg. Peso de ', end='')
menorNomes = list()
for p in pessoas:
    if p[1] == menor:
        menorNomes.append(p[0])

tam = len(menorNomes)
for pos, m in enumerate(menorNomes):
    if tam == 1 or pos == tam - 1:
        print(f'{m}.')
    elif pos < tam - 2:
        print(f'{m}, ', end='')
    elif pos == tam - 2:
        print(f'{m} e ', end='')

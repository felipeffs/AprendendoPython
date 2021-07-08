numeros = []
pares = []
impares = []

quantidade = 0
while True:
    for n in range(0, quantidade):
        while True:
            valor = input('-> ')
            if valor.isdigit():
                valor = int(valor)
                numeros.append(valor)
                break
            print('\033[31mNúmero Inválido! Digite um número inteiro...\033[m')
    while True:
        quantidade = input('Deseja adicionar quantos números? ')
        if quantidade.isdigit():
            quantidade = int(quantidade)
            break
        print('\033[31mNúmero Inválido! Digite uma quantidade inteira...\033[m')
    if quantidade == 0:
        break
for n in numeros:
    if n % 2 == 0:
        pares.append(n)
    else:
        impares.append(n)
print(f'{"Resultados":=^50}')
print(f'Todos os números: {numeros}')
print(f'Todos os números pares: {pares}')
print(f'Todos os números ímpares: {impares}')

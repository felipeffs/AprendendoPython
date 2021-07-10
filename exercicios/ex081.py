numeros = []
quant = add = 0
while True:
    for n in range(0, quant):
        while True:
            add = str(input('-> '))
            if add.isdigit():
                add = int(add)
                numeros.append(add)
                break
            print('\033[31mNúmero inválido! Digite um número inteiro.\033[m')
    while True:
        quant = str(input('Deseja digitar quantos números? '))
        if quant.isdigit():
            quant = int(quant)
            break
        print('\033[31mQuantidade inválida! Digite um valor inteiro.\033[m')
    if quant == 0:
        break

numeros.sort(reverse=True)
print('='*50)
print(f'{"Informações":^50}')
print('='*50)
print(f'Números digitados: {len(numeros)}')
print(f'Lista decrescente: {numeros}')
print('O valor 5 faz parte da lista' if 5 in numeros else 'O valor 5 não faz parte da lista')

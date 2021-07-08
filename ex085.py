lista = [[], []]

for v in range(0, 7):
    while True:
        b = str(input(f'Digite o {v + 1}º valor inteiro: '))
        if b.isdigit():
            b = int(b)
            if b % 2 == 0:
                lista[0].append(b)
            else:
                lista[1].append(b)
            break
        print('\033[31mValor inválido! Digite novamente.\033[m')
print(f'Os valores pares digitados foram: {sorted(lista[0])}'
      f'\nOs valores ímpares digitados foram: {sorted(lista[1])}')

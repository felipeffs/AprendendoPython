matriz = []
print('='*50)
for coluna in range(0, 3):
    matriz.append(list())
    for linha in range(0, 3):
        matriz[coluna].append(int(input(f'Digite o valor para [{coluna}, {linha}]: ')))
print('='*50)
for coluna in range(0, 3):
    for linha in range(0, 3):
        if linha == 2:
            print(f'[{matriz[coluna][linha]:^5}]')
        else:
            print(f'[{matriz[coluna][linha]:^5}] ', end='')
print('='*50)

somaPar = somarColuna3 = maiorLinha2 = 0
for pos, linha in enumerate(matriz):
    for posColuna, n in enumerate(linha):
        if n % 2 == 0:
            somaPar += n
        if pos == 1:
            if posColuna == 0 or maiorLinha2 < n:
                maiorLinha2 = n
        if posColuna == 2:
            somarColuna3 += n

print(f'A soma de todos os valores pares digitados foi {somaPar}')
print(f'A Soma dos valores da terceira coluna foi {somarColuna3}')
print(f'O maior valor da segunda linha foi {maiorLinha2}')
print('='*50)

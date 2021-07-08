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

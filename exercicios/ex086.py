"""
Crie um programa que crie uma matriz de dimensão 3x3 e preencha com valores lidos
pelo teclado. No final, mostre a matriz na tela, com a formatação correta.
"""

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

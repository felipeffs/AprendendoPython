"""
Faça um programa que mostre a tabuada de vários números, um de cada vez,
para cada valor digitado pelo usuário. O programa será interrompido quando
o número solicitado for negativo.
"""

print(f'{"Programa=Tabuada":=^40}')

while True:
    print('='*40)
    n = int(input('Deseja ver a tabuada de qual número? '))
    if n < 0:
        print('\033[:34mPrograma Tabuada Finalizado\033[m')
        break
    for c in range(1, 11):
        print(f'{f"{c} X {n} = {c * n}":^34}')

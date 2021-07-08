from random import randint
from time import sleep
print('='*50)
print(f'{"Gerador de Palpites para MEGA SENA":^50}')
print('='*50)
while True:
    quant = input('Deseja gerar quantos palpites? ')
    if quant.isdigit():
        quant = int(quant)
        break

print(f'{f"SORTEANDO {quant} JOGOS" if quant > 1 else f"SORTEANDO O JOGO":—^50}')
palpites = []
for coluna in range(0, quant):
    palpites.append(list())
    for linha in range(0, 6):
        while True:
            numero = randint(1, 60)
            if numero not in palpites[coluna]:
                palpites[coluna].append(numero)
                break
    sleep(1)
    print('\033[33m-\033[m'*50)
    print(f'{f"JOGO {coluna + 1}":^50}')
    print(f'{str(palpites[coluna]):^50}')
print('\033[33m-\033[m'*50)
print(f'{"Boa Sorte!":—^50}')
print('='*50)

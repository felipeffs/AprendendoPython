from random import randint
from time import sleep
jogadores = {}
print('—'*50)
print(f'{"Valores Sorteados":^50}')
print('—'*50)
for j in range(1, 5):
    jogadores[f'Jogador {j}'] = randint(1, 6)
    sleep(1)
    print(f"\t\t\t   O jogador {j} tirou {jogadores[f'Jogador {j}']}")
print('—'*50)
print(f'{"Raking dos Jogadores":^50}')
print('—'*50)
pos = 0
for j in sorted(jogadores, key=jogadores.get, reverse=True):
    pos += 1
    sleep(1)
    print(f'{f"{pos}º lugar: {j} com {jogadores[j]}":^50}')
print('—'*50)

# Ordenar dicionário:
# ranking = dict()
# for j in sorted(jogadores, key=jogadores.get, reverse=True):
#     ranking[j] = jogadores[j]
# print(ranking)

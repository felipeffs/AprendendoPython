"""
Crie um programa que gerencie o aproveitamento de um jogador de futebol. O programa
vai ler o nome do jogador e quantas partidas ele jogou. Depois vai ler a quantidade
de gols feitos em cada partida. No final, tudo isso será guardado em um dicionário,
incluindo o total de gols feitos durante o campeonato.
"""

jogador = dict()
print('='*50)
while True:
    jogador['Nome'] = str(input('Nome do jogador: ')).strip().title()
    nome = jogador['Nome'].replace(' ', '')
    if nome.isalpha():
        break
    print('\033[31mNome Inválido! Digite novamente.\033[m')
print('='*50)
while True:
    quant = str(input(f'Quantas partidas {jogador["Nome"]} jogou? ')).strip()
    if quant.isdigit():
        quant = int(quant)
        break
    print('\033[31mQuantidade Inválida! Digite novamente.\033[m')
print('='*50)
gols = list()
total = 0
for partida in range(0, quant):
    while True:
        g = str(input(f'Quantos gols na partida {partida + 1}? ')).strip()
        if g.isdigit():
            gols.append(int(g))
            total += int(g)
            print('—'*50)
            break
        print('\033[31mQuantidade inválida! Digite novamente.\033[m')
jogador['Gols'] = gols[:]
jogador['Total'] = total
print(jogador)

print('='*50)
for k, v in jogador.items():
    print(f'{k}: {v}')

print('='*50)
print(f'O jogador {jogador["Nome"]} jogou {len(jogador["Gols"])} partidas.')
for pos, p in enumerate(jogador["Gols"]):
    print(f'\t => Na partida {pos + 1}, fez {p} gols.')
print(f'Foi um total de {jogador["Total"]} gols.')

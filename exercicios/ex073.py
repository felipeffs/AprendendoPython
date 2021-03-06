"""
Crie uma tupla preenchida com os 20 primeiros colocados da Tabela do
Campeonanto Brasileiro de Futebol, na ordem de colocação. Depois mostre:
A) Os 5 primeiros.
B) Os últimos 4 colocados.
C) Times em ordem alfabética.
D) Em que posição está o time da Chapecoense.
"""

# Colocação do dia 01/06/2021
colocados = 'Bragantino', 'Bahia', 'Ceará SC', 'Fortaleza', 'Athletico-PR', 'Flamengo', 'Atlético-GO', \
            'Sport Recife', 'Juventude', 'Cuiabá', 'Internacional', 'São Paulo', 'Fluminense', \
            'Grêmio', 'Atlético-MG', 'América-MG', 'Palmeiras', 'Corinthians', 'Chapecoense', 'Santos'

print('-='*50)
print('Lista de Times do Brasileirão')
for pos, c in enumerate(colocados):
    print(f'{pos + 1}º', c)
print('-='*50)
print(f'Os 5 primeiros são {colocados[:5]}')
print('-='*50)
print(f'Os 4 últimos são {colocados[-4:]}')
print('-='*50)
print('Times em Ordem Alfabética')
for c in sorted(colocados):
    print(c)
print('-='*50)
print(f'O Chapecoense está em {colocados.index("Chapecoense") + 1}º lugar')

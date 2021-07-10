"""
Desenvolva um programa que pergunte a distância de uma viagem em Km.
Calcule o preço da passagem, cobrando R$0,50 por Km para viagens de
até 200Km e R$0,45 para viagens mais longas.
"""

d = float(input('Distância da viagem em km: '))

custo = d * 0.5 if d <= 200 else d * 0.45

print('A passagem vai custar R${:.2f}'.format(custo))

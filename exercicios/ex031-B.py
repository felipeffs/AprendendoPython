d = float(input('Distância da viagem em km: '))

custo = d * 0.5 if d <= 200 else d * 0.45

print('A passagem vai custar R${:.2f}'.format(custo))
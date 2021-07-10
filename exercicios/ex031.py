d = float(input('Distância da viagem em km: '))

if d <= 200:
    custo = d * 0.5
else:
    custo = d * 0.45

print('A passagem vai custar R${:.2f}'.format(custo))

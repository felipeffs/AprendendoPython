menorPeso = 0
maiorPeso = 0
print('=='*22)
for c in range(1, 6):
    p = float(input('Digite o peso da {}ª pessoa: '.format(c)))
    if c == 1:
        menorPeso = p
        maiorPeso = p
    elif menorPeso > p:
        menorPeso = p
    elif maiorPeso < p:
        maiorPeso = p

print('\nINFO! Menor peso: {} || Maior peso: {}'.format(menorPeso, maiorPeso))
print('=='*22)

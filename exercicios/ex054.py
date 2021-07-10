from datetime import date
maiores = 0
menores = 0

for c in range(0, 7):
    nasc = int(input('Digite o ano de nascimento da {}ª pessoa: '.format(c + 1)))
    idade = date.today().year - nasc
    if idade >= 21:
        maiores += 1
    else:
        menores += 1
print('\nDos 7, {} são maiores de idade enquanto {} são menores de idade'.format(maiores, menores))

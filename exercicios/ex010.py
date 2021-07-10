"""
Crie um programa que leia quanto dinheiro uma pessoa tem na
carteira e mostre quantos dólares ela pode comprar.

Considere U$1,00 = 5,48 (Início de 2021)
"""

carteira = float(input('Quantos reais tem na carteira? '))
cD = 5.48
dolarCompra = carteira/cD
print('Você pode comprar {:.2f} doláres!'.format(dolarCompra))

"""
Faça um algoritmo que leia o preço de um produto e mostre seu
novo preço, com 5% de desconto.
"""

preco = float(input('Qual o preço do produto? R$'))
preco = preco * 0.95
print('Com 5% de desconto fica por apenas R${:.2f}'.format(preco))

"""
Escreva um programa que pergunte a quantidade de Km
percorridos por um carro alugado e a quantidade de dias pelos
quais ele foi alugado. Calcule o preço a pagar, sabendo que o carro
custa R$60 por dia e R$0,15 por Km rodado.
"""

diaAlugado = int(input('Por quantos dias o carro foi alugado? '))
kmRodado = float(input('Quantos quilômetros foram percorridos '))

custo = 60 * diaAlugado + kmRodado * 0.15

print('O custo foi de R${:.2f}'.format(custo))

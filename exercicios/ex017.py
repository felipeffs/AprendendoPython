"""
Faça um programa que leia o comprimento do cateto oposto e do
cateto adjacente de um triângulo, calcule e mostre o comprimento
da hipotenusa.
"""

from math import pow, sqrt

print('>> Calcular a hipotenusa de um triângulo retângulo')
catOp = float(input('Informe o comprimento do cateto oposto: '))
catAdj = float(input('Informe o comprimento do cateto adjacente: '))
h = sqrt(float(pow(catOp, 2) + pow(catAdj, 2)))
print('A hipotenusa de um triângulo retângulo com o comprimento do cateto oposto {:.2f} '
      '\ne do cateto adjacente {:.2f} é... {:.2f}'.format(catOp, catAdj, h))

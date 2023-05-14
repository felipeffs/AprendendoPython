"""
Crie um algoritmo que leia um número e mostre o seu dobro, triplo e
raiz quadrada.
"""

n = int(input('Digite um Número: '))
print('O Número é {}'
      '\nDobro: {}'
      '\nTriplo: {}'
      '\nRaiz Quadrada {:.2f}'.format(n, n*2, n*3, n**(1/2)))

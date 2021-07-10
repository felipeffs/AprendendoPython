"""
Desenvolva um programa que leia o comprimento de três retas
e diga ao usuário se elas podem ou não formar um triângulo.
"""

print('-='*20)
print('Analisando triângulos')
print('-='*20)
c1 = float(input('Comprimento da reta 1: '))
c2 = float(input('Comprimento da reta 2: '))
c3 = float(input('Comprimento da reta 3: '))

r = 'Não da pra formar um triângulo'
if c3 < (c1 + c2):
    if c3 > (c1 - c2):
        r = 'Da pra formar um triângulo!'
print(r)

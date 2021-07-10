"""
Faça um programa que leia um ângulo qualquer e mostre na tela o
valor do seno, cosseno e tangente desse ângulo.
"""

import math

an = float(input('Informe o ângulo: '))
an = math.radians(an)
print('Seno {:.2f}, Cosseno {:.2f}, Tangente {:.2f}'.format(math.sin(an), math.cos(an), math.tan(an)))

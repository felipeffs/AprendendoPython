"""
Faça um programa que tenha uma função área(), que receba as dimensões de um terreno
retangular (largura e comprimento) e mostre a área do terreno.
"""


def area(largura, comprimento):
    a = largura * comprimento
    print(f'A área de um terreno {largura:.2f}m por {comprimento:.2f}m é de {a:.2f}m²')


print(f'{"Controle de Terrenos":-^50}')
l = float(input('Largura (m): '))
c = float(input('Comprimento (m): '))
print('-'*50)
area(l, c)
print('-'*50)

"""
Faça um programa que leia a largura e a altura de uma parede em
metros, calcule a sua área e a quantidade de tinta necessária para
pintá-la, sabendo que cada litro de tinta, pinta uma área de 2m².
"""

altura = float(input('Qual a altura da parede? '))
largura = float(input('e a largura? '))
areaP = altura * largura
tintaN = areaP / 2
print('A área da parede informada é de {:.2f}m² e será necessário {:.2f}L de tinta para pintá-la'.format(areaP, tintaN))

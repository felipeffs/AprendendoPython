from math import hypot

catOp = float(input('>> Calcular a hipotenusa de um triângulo retângulo \nInforme o comprimento do cateto oposto: '))
catAdj = float(input('Informe o comprimento do cateto adjacente: '))
h = hypot(catOp, catAdj)
print('A hipotenusa de um triângulo retângulo com o comprimento do cateto oposto {:.2f} '
      '\ne do cateto adjacente {:.2f} é... {:.2f}'.format(catOp, catAdj, h))

from math import pow, sqrt

catOp = float(input('>> Calcular a hipotenusa de um triângulo retângulo \nInforme o comprimento do cateto oposto: '))
catAdj = float(input('Informe o comprimento do cateto adjacente: '))
h = sqrt(float(pow(catOp, 2) + pow(catAdj, 2)))
print('A hipotenusa de um triângulo retângulo com o comprimento do cateto oposto {:.2f} '
      'e do cateto adjacente {:.2f} é... {:.2f}'.format(catOp, catAdj, h))

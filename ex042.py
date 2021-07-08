print('-='*20)
print('Analisador triângulos Aprimorado')
print('-='*20)
c1 = float(input('Comprimento da reta 1: '))
c2 = float(input('Comprimento da reta 2: '))
c3 = float(input('Comprimento da reta 3: '))

if c1 < c2 + c3 and c2 < c1 + c3 and c3 < c1 + c2:
    if c1 == c2 == c3:
        print('Da pra formar um triângulo equilátero')
    elif c1 == c2 or c2 == c3 or c1 == c3:
        print('Da pra formar um triângulo isósceles')
    else:
        print('Da pra formar um triângulo escaleno')
else:
    print('Não da pra formar um triângulo!')

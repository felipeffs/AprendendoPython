print('-='*20)
print('Analisando triângulos (LADO B)')
print('-='*20)
c1 = float(input('Comprimento da reta 1: '))
c2 = float(input('Comprimento da reta 2: '))
c3 = float(input('Comprimento da reta 3: '))

if c1 < c2 + c3 and c2 < c1 + c3 and c3 < c1 + c2:
    print('Da pra formar um triângulo!')
else:
    print('Não da pra formar um triângulo!')

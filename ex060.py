print('>Fatorial')
n = int(input(' Digite um número: '))
p = n
fatorial = n
while p != 1:
    p -= 1
    fatorial *= p
print('O Fatorial de {} é igual a {}'.format(n, fatorial))

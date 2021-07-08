print('>Fatorial')
n = int(input(' Digite um número: '))
f = n
for c in range(1, n):
    f *= c
print('Fatorial de {} é igual a {}'.format(n, f))
